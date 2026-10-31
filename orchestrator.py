
"""Round orchestration with shared-context snapshots and slot isolation."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable, Iterable
from uuid import uuid4

from .models import (
    ConversationEvent,
    MemberOutcome,
    MemberReply,
    MemberRequest,
    MemberSpec,
    MemoryOperationCheck,
    MemoryRecoveryResult,
    MemoryUpdate,
    MemoryVersion,
    MemoryWriteResult,
    RoundResult,
    SlotMemory,
    MemoryStore,
)


MemberInvoker = Callable[[MemberRequest], MemberReply]

RECOVERABLE_STATUSES = {
    "pending",
    "save_failed",
    "confirmation_failed",
}

STORE_WRITE_STATUSES = {
    "pending",
    "saved",
    "save_failed",
    "confirmation_failed",
}


class RoundOrchestrator:
    """Run enabled slots independently against one pre-round snapshot."""

    @staticmethod
    def _activate_confirmed_write(
        *,
        slot_memory: SlotMemory,
        update: MemoryUpdate,
        operation_id: str,
        revision: int | None,
    ) -> tuple[MemoryWriteResult, SlotMemory]:
        """Activate a confirmed write exactly once."""

        if revision is None:
            return (
                MemoryWriteResult(
                    status="confirmation_failed",
                    update=update,
                    operation_id=operation_id,
                    error="Confirmed write has no revision.",
                ),
                slot_memory,
            )

        matching_versions = [
            version
            for version in slot_memory.versions
            if version.operation_id == operation_id
        ]

        if matching_versions:
            existing = matching_versions[0]

            if (
                len(matching_versions) == 1
                and existing.revision == revision
                and existing.action == update.action
                and existing.content == update.content
            ):
                return (
                    MemoryWriteResult(
                        status="saved",
                        update=update,
                        operation_id=operation_id,
                        revision=revision,
                    ),
                    slot_memory,
                )

            return (
                MemoryWriteResult(
                    status="confirmation_failed",
                    update=update,
                    operation_id=operation_id,
                    revision=revision,
                    error="Operation ID conflicts with existing memory history.",
                ),
                slot_memory,
            )

        latest = slot_memory.latest

        if latest is not None and revision <= latest.revision:
            return (
                MemoryWriteResult(
                    status="confirmation_failed",
                    update=update,
                    operation_id=operation_id,
                    revision=revision,
                    error="Stored revision does not advance slot memory.",
                ),
                slot_memory,
            )

        new_version = MemoryVersion(
            revision=revision,
            action=update.action,
            content=update.content,
            operation_id=operation_id,
        )

        updated_memory = SlotMemory(
            slot_id=slot_memory.slot_id,
            versions=slot_memory.versions + (new_version,),
        )

        return (
            MemoryWriteResult(
                status="saved",
                update=update,
                operation_id=operation_id,
                revision=revision,
            ),
            updated_memory,
        )

    def recover_memory_operation(
        self,
        *,
        slot_id: str,
        memory_result: MemoryWriteResult,
        slot_memory: SlotMemory,
        memory_store: MemoryStore,
    ) -> MemoryRecoveryResult:
        """Recover one uncertain memory operation."""

        update = memory_result.update
        operation_id = memory_result.operation_id

        def unresolved(error: str) -> MemoryRecoveryResult:
            return MemoryRecoveryResult(
                memory_result=MemoryWriteResult(
                    status="confirmation_failed",
                    update=update,
                    operation_id=operation_id,
                    error=error,
                ),
                slot_memory=slot_memory,
            )

        if slot_memory.slot_id != slot_id:
            return unresolved("Slot ID does not match the supplied memory.")

        if memory_result.status not in RECOVERABLE_STATUSES:
            return unresolved("Memory result is not in a recoverable state.")

        if update is None or update.action == "no_change":
            return unresolved("A valid memory update is required for recovery.")

        if not operation_id:
            return unresolved("Recovery requires the original operation ID.")

        # First inspect the original operation.
        try:
            check = memory_store.check(operation_id)

            if not isinstance(check, MemoryOperationCheck):
                return unresolved("MemoryStore.check returned an invalid result.")

        except Exception as exc:
            return unresolved(
                f"Operation check failed: {type(exc).__name__}: {exc}"
            )

        if check.status == "saved":
            result, updated_memory = self._activate_confirmed_write(
                slot_memory=slot_memory,
                update=update,
                operation_id=operation_id,
                revision=check.revision,
            )

            if check.error:
                result = MemoryWriteResult(
                    status=result.status,
                    update=update,
                    operation_id=operation_id,
                    revision=result.revision,
                    error=check.error,
                )

            return MemoryRecoveryResult(
                memory_result=result,
                slot_memory=updated_memory,
            )

        if check.status == "unknown":
            return unresolved(
                check.error or "Storage cannot determine the operation status."
            )

        if check.status != "not_found":
            return unresolved("MemoryStore.check returned an unknown status.")

        # Contract: not_found guarantees that the operation was not committed.
        # Retry with the SAME operation ID.
        try:
            write_result = memory_store.save(
                slot_id,
                update,
                operation_id,
            )
        except Exception as exc:
            return unresolved(
                f"Retry outcome is uncertain: {type(exc).__name__}: {exc}"
            )

        if not isinstance(write_result, MemoryWriteResult):
            return unresolved("MemoryStore.save returned an invalid result.")

        if write_result.status == "saved":
            result, updated_memory = self._activate_confirmed_write(
                slot_memory=slot_memory,
                update=update,
                operation_id=operation_id,
                revision=write_result.revision,
            )

            return MemoryRecoveryResult(
                memory_result=result,
                slot_memory=updated_memory,
            )

        if write_result.status not in STORE_WRITE_STATUSES - {"saved"}:
            return unresolved("MemoryStore.save returned an invalid write status.")

        return MemoryRecoveryResult(
            memory_result=MemoryWriteResult(
                status=write_result.status,
                update=update,
                operation_id=operation_id,
                error=write_result.error,
                revision=write_result.revision,
            ),
            slot_memory=slot_memory,
        )

    def run_round(
        self,
        *,
        round_index: int,
        current_user_message: str,
        shared_context: Iterable[ConversationEvent],
        members: Iterable[MemberSpec],
        slot_memories: Iterable[SlotMemory],
        invoke_member: MemberInvoker,
        memory_store: MemoryStore,
    ) -> RoundResult:

        context_snapshot = tuple(shared_context)
        enabled_members = tuple(member for member in members if member.enabled)
        memory_by_slot = {memory.slot_id: memory for memory in slot_memories}

        if len({member.slot_id for member in enabled_members}) != len(enabled_members):
            raise ValueError("Enabled member slot_id values must be unique.")

        requests: dict[str, MemberRequest] = {}

        for member in enabled_members:
            requests[member.slot_id] = MemberRequest(
                round_index=round_index,
                slot_id=member.slot_id,
                model=member.model,
                role=member.role,
                current_user_message=current_user_message,
                shared_context=context_snapshot,
                slot_memory=memory_by_slot.get(
                    member.slot_id,
                    SlotMemory(slot_id=member.slot_id),
                ),
            )

        outcomes_by_slot: dict[str, MemberOutcome] = {}

        if enabled_members:
            with ThreadPoolExecutor(max_workers=len(enabled_members)) as executor:
                future_to_slot = {
                    executor.submit(
                        invoke_member,
                        requests[member.slot_id],
                    ): member.slot_id
                    for member in enabled_members
                }

                for future in as_completed(future_to_slot):
                    slot_id = future_to_slot[future]

                    try:
                        reply = future.result()

                        if not isinstance(reply, MemberReply):
                            raise TypeError(
                                "Member invoker must return MemberReply."
                            )

                        outcomes_by_slot[slot_id] = MemberOutcome(
                            slot_id=slot_id,
                            response=reply.response,
                            memory_update=reply.memory_update,
                        )

                    except Exception as exc:
                        outcomes_by_slot[slot_id] = MemberOutcome(
                            slot_id=slot_id,
                            error=f"{type(exc).__name__}: {exc}",
                        )

        outcomes = tuple(
            outcomes_by_slot[member.slot_id]
            for member in enabled_members
        )

        updated_memories = dict(memory_by_slot)
        finalized_outcomes: list[MemberOutcome] = []

        for outcome in outcomes:
            update = outcome.memory_update

            if outcome.error is not None:
                finalized_outcomes.append(outcome)
                continue

            if update is None:
                finalized_outcomes.append(
                    MemberOutcome(
                        slot_id=outcome.slot_id,
                        response=outcome.response,
                        memory_result=MemoryWriteResult(
                            status="not_produced",
                        ),
                    )
                )
                continue

            if update.action == "no_change":
                finalized_outcomes.append(
                    MemberOutcome(
                        slot_id=outcome.slot_id,
                        response=outcome.response,
                        memory_update=update,
                        memory_result=MemoryWriteResult(
                            status="no_change",
                            update=update,
                        ),
                    )
                )
                continue

            operation_id = str(uuid4())

            try:
                write_result = memory_store.save(
                    outcome.slot_id,
                    update,
                    operation_id,
                )

                if not isinstance(write_result, MemoryWriteResult):
                    raise TypeError(
                        "MemoryStore.save must return MemoryWriteResult."
                    )

                if write_result.status not in STORE_WRITE_STATUSES:
                    raise ValueError(
                        "MemoryStore.save returned an invalid write status."
                    )

                if write_result.status == "saved":
                    prior = updated_memories.get(
                        outcome.slot_id,
                        SlotMemory(slot_id=outcome.slot_id),
                    )

                    memory_result, updated_memory = self._activate_confirmed_write(
                        slot_memory=prior,
                        update=update,
                        operation_id=operation_id,
                        revision=write_result.revision,
                    )

                    updated_memories[outcome.slot_id] = updated_memory

                else:
                    memory_result = MemoryWriteResult(
                        status=write_result.status,
                        update=update,
                        operation_id=operation_id,
                        error=write_result.error,
                        revision=write_result.revision,
                    )

            except Exception as exc:
                # An exception does not prove that the write was not committed.
                memory_result = MemoryWriteResult(
                    status="confirmation_failed",
                    update=update,
                    operation_id=operation_id,
                    error=f"{type(exc).__name__}: {exc}",
                )

            finalized_outcomes.append(
                MemberOutcome(
                    slot_id=outcome.slot_id,
                    response=outcome.response,
                    memory_update=update,
                    memory_result=memory_result,
                )
            )

        user_event = ConversationEvent(
            event_id=str(uuid4()),
            round_index=round_index,
            kind="user",
            content=current_user_message,
        )

        committed_events = [user_event]

        for outcome in finalized_outcomes:
            if outcome.error is not None:
                continue

            if outcome.response is not None:
                committed_events.append(
                    ConversationEvent(
                        event_id=str(uuid4()),
                        round_index=round_index,
                        kind="member",
                        content=outcome.response,
                        slot_id=outcome.slot_id,
                    )
                )

        return RoundResult(
            round_index=round_index,
            shared_context=context_snapshot + tuple(committed_events),
            outcomes=tuple(finalized_outcomes),
            slot_memories=tuple(
                updated_memories[key]
                for key in sorted(updated_memories)
            ),
        )
