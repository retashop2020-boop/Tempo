# Ilan Agent Runner — System Design

**Status:** Architecture and implementation snapshot  
**Snapshot date:** 2026-11-01  
**Implementation baseline:** Local Runner repository, latest reported commit `8942e4b`, with subsequent uncommitted FileTools and documentation work.

> This file is intended to be transferred into the separate local Runner repository as `design.md`. It is stored temporarily in the Tempo repository only to make the two-document handover convenient. Tempo is not the Runner runtime or source repository.

---

## 1. Purpose

Ilan Agent Runner is a local, bounded execution system for a future software-development agent.

Its purpose is to let an agent inspect a designated project, plan changes, request narrowly scoped file operations, execute tests in a controlled environment, analyze actual results, and attempt a limited number of repairs.

The Runner is the authority boundary between the agent and the machine. The agent can reason and request; the Runner validates permissions, performs operations, records evidence, and controls the lifecycle.

The first implementation is a local CLI and modular Python codebase. It is not tied to an LLM, model provider, API, or UI.

## 2. Core principles

1. **Authority stays outside the agent.** The agent cannot grant permissions, expand its workspace, alter limits, or decide unilaterally that a Run succeeded.
2. **Least Privilege / Default Deny.** Every tool has an explicit permission requirement. Unknown tools are denied.
3. **Separation of responsibilities.** Planning, filesystem access, authorization, execution, lifecycle, and evidence collection remain separate modules.
4. **Evidence-based completion.** Agent claims are not execution evidence. The Runner decides status from actual operations and test results.
5. **Bounded autonomy.** The agent may iterate within a Runner-enforced repair budget but cannot extend that budget.
6. **User control over consequential actions.** No purchase, financial commitment, commit, push, merge, publication, or other consequential action without explicit user authorization.
7. **Model independence.** The core Runner must work and be tested without an LLM. A model adapter is a later layer.

A guiding constraint for the agent is: **freedom in problem-solving; no independent authority to expand permissions or spend money.**

## 3. System boundary and component responsibilities

| Component | Responsibility | Authority |
|---|---|---|
| User | Defines task, workspace, permissions, budget, approval boundaries | Highest project-level authority |
| Ilan agent | Understands the task, prepares plans, requests tools, analyzes evidence | Only the capabilities exposed by Runner |
| Runner core | Validates requests, authorizes tools, executes operations, records evidence, controls lifecycle | Enforces system policy |
| Workspace tools | Perform bounded file operations | Only paths and operations permitted by Runner |
| Docker | Executes project code and tests in a constrained environment | No independent authority |
| Model adapter (future) | Sends context and requests to a chosen model/provider | No authority beyond Runner interface |
| Igor documentation role | Maintains decisions, implementation state, and handover consistency | Documentation/review role, not runtime authority |

The agent must not receive unrestricted terminal access or direct access to Runner internals.

## 4. High-level architecture

The intended dependency direction is:

```text
User
 |
 v
Runner CLI / orchestration
 |
 +--> Run lifecycle
 |
 +--> Permission policy
 |
 +--> Agent-facing tool facade
 |      |
 |      +--> FileTools
 |      |      |
 |      |      +--> WorkspaceBoundary
 |      |
 |      +--> Git read tools (future)
 |      |
 |      +--> Test execution tool (future)
 |
 +--> Operation records
 |
 +--> TraceCollector
 |
 +--> Docker execution adapter (future)
 |
 +--> Model adapter (future; replaceable)
```

The current codebase has the core data structures, permission policy, trace collector, workspace boundary, and two read tools. The complete orchestration and adapter connections are not yet implemented.

### Module boundaries

| Module | Intended responsibility |
|---|---|
| `core/ids.py` | Runner-generated identifiers |
| `core/run.py` | Run lifecycle and repair-cycle state |
| `core/operation.py` | One tool invocation record |
| `core/trace.py` | Three JSONL evidence streams |
| `core/permissions.py` | Permission levels, tool mapping, authorization policy |
| `core/workspace.py` | Descriptor-relative workspace path boundary |
| `core/file_tools.py` | Workspace-bounded file operations |
| `main.py` | Local CLI entry point and future composition root |

The agent-facing facade is a future component. It must not expose mutable internal objects or administrative methods directly.

## 5. Tool interface and capability model

The intended named tools are:

| Tool | Permission | Status at snapshot |
|---|---|---|
| `list_files` | READ | Implemented |
| `read_file` | READ | Implemented |
| `write_file` | WRITE | Not implemented |
| `apply_patch` | WRITE | Not implemented |
| `git_status` | READ | Not implemented |
| `git_diff` | READ | Not implemented |
| `run_tests` | EXECUTE | Not implemented |
| `collect_logs` | READ | Not implemented |
| `inspect_traces` | READ | Not implemented |

The current `PermissionPolicy` mapping may contain entries for future tools before their implementations exist. A permission mapping is not proof that a tool is implemented or callable.

### Permission levels

- `READ`: inspect allowed project files and state.
- `WRITE`: create or modify allowed project files.
- `EXECUTE`: run explicitly permitted commands or tests.

WRITE does not imply EXECUTE.

Unknown tools are denied by default. The agent cannot call `grant()` or `revoke()`. These methods belong to administrative Runner control and must not be exposed through the agent facade.

### Tool execution contract

Every tool call should eventually pass through one Runner-controlled path:

1. Validate the tool name and input schema.
2. Generate a unique `operation_id`.
3. Check the required permission.
4. Record a denied operation if authorization fails.
5. Invoke the tool using Runner-controlled arguments and resource limits.
6. Capture the actual result or exception.
7. Finalize the Operation exactly once.
8. Record execution evidence in Trace.
9. Return a bounded, structured result to the agent.

This contract is a design target; automatic integration is not implemented yet.

## 6. Identity and data contracts

### Identifiers

- `run_id`: one complete development cycle.
- `request_id`: one main agent request within a Run.
- `operation_id`: one specific tool invocation.
- `parent_operation_id`: optional link to a genuinely dependent operation.
- `agent_id`: identity of the requesting agent.
- `tool`: tool name.

The Runner generates identifiers. The agent must not choose or overwrite them.

### Operation record

An Operation is expected to contain:
- `run_id`
- `request_id`
- `operation_id`
- `parent_operation_id`
- `agent_id`
- `tool`
- `started_at`
- `finished_at`
- `status`
- `result`
- `error`

Statuses:
- `success`
- `error`
- `denied`
- `timeout`
- `cancelled`

The exact semantic rule for whether a non-success Operation may contain both `result` and `error` remains to be finalized. Keep this explicit during future schema work rather than silently assuming one interpretation.

## 7. Run lifecycle and orchestration

A Run represents one end-to-end development task.

Statuses:
- `running` — active internal state.
- `completed` — success criteria are established by evidence.
- `failed` — repair budget exhausted with failing tests.
- `timeout`
- `cancelled`
- `blocked`
- `inconclusive` — tests pass but the requested goal is not established.

### Repair budget

The initial test run may fail. The agent may then perform at most three repair cycles.

- Maximum repair cycles: 3.
- Maximum test executions in one Run: 4.
- The Runner enforces these limits.
- The agent cannot extend or reset the budget.
- A test pass alone does not prove the requested goal was achieved.
- If tests pass but goal completion is not established, the Run is `inconclusive`.

### Intended lifecycle

1. Runner creates the Run and generates `run_id`.
2. Agent receives the task.
3. Agent reads workspace context using READ tools.
4. Agent submits a structured Plan:
   - Goal
   - Target files
   - Steps
   - Assumptions
   - Risks
   - Success criteria
5. Runner records and validates the Plan; validation does not grant permissions.
6. Agent requests a named tool.
7. Runner authorizes and records the Operation.
8. Runner invokes the tool and records the actual outcome.
9. Runner runs tests through a permitted Docker execution path.
10. Test results are recorded.
11. Agent analyzes the evidence.
12. On failure, agent may repair and retry within the fixed budget.
13. Runner evaluates stopping conditions and final status.
14. Runner produces a report containing goal, plan, changed files, tests, result, iteration count, errors, and identifiers.

The agent cannot finish a Run by asserting success. The Runner owns finalization.

### Stopping conditions

- Success criteria established.
- Repair budget exhausted.
- Timeout.
- User cancellation.
- Security or permission block.
- Other explicit Runner-controlled stop condition.

A global Run timeout is intended to be configurable, but its default value has not yet been decided. The agent must not be allowed to extend it.

## 8. Trace and evidence architecture

Each Run gets a separate directory:

```text
traces/<run_id>/
    agent_trace.jsonl
    execution_trace.jsonl
    test_trace.jsonl
```

### Agent Trace

Captures agent-side decisions and requests:
- Plan.
- Assumptions.
- Requested tools.
- Reasons for choices.

It answers: **Why did the agent request this action?**

### Execution Trace

Captures Runner-observed events:
- Tool invocation.
- Operation identifiers.
- Timestamps.
- Authorization decisions.
- Exceptions.
- Actual result/error information.

It answers: **What did the Runner actually do?**

### Test Trace

Captures:
- Test command/execution metadata.
- Test outcome.
- Assertion failures.
- Relevant artifacts.

It answers: **What did the tests establish?**

### Trace rules

- Shared identifiers link related events across streams.
- Actual execution events must be emitted by Runner code.
- Agent explanations are not a substitute for execution evidence.
- Tool calls, file changes, tests, errors, permission denials, and timing must be recorded.
- Trace level is one of `minimal`, `normal` (default), or `debug`.
- User/Runner configuration controls trace level; agent cannot reduce it.
- Existing traces are not agent-editable or agent-deletable.
- Full file contents should not be duplicated into traces by default. Prefer hashes and diffs where appropriate.

Current TraceCollector behavior is append-only JSONL writing with flush. It is not tamper-proof and does not guarantee durability after sudden power loss. Locking and concurrent writer behavior are not yet established; v1 Runs are sequential.

## 9. Workspace boundary and filesystem security

### Workspace model

The agent receives access only to a configured project workspace. The current sample workspace is:

```text
~/ilan-lab/workspace/sample-project
```

The agent must not access:
- Runner configuration.
- Logs and traces.
- Other user-home files.
- Secrets or API keys.
- Unapproved network resources.

### Linux `openat2` boundary

`WorkspaceBoundary` uses Linux `openat2` and a retained root directory descriptor.

Current implementation details:
- System call number 437 on the tested x86_64 Linux environment.
- `RESOLVE_BENEATH`.
- `RESOLVE_NO_MAGICLINKS`.
- Relative symlinks are allowed only when resolution remains beneath the root.
- Absolute symlinks are rejected.
- Absolute user paths and `..` traversal are rejected.
- Actual file operations use `open_file()`.

`resolve()` is for inspection only and must not be treated as a secure open operation. A later filesystem action must use the descriptor-relative boundary.

### Threat-model limitations

This boundary is not a complete filesystem sandbox.

- Hard links are not restricted by `openat2` path resolution.
- The workspace root is trusted at initialization.
- Internal callers control open flags; those flags must never be agent-controlled.
- A path inspection followed by a separate path-based open would reintroduce a race and is prohibited.
- Some special device files can have effects during open before the code checks file type.
- The current implementation has been tested under WSL2; do not assume portability to non-Linux systems or kernels without `openat2`.

## 10. FileTools implementation snapshot

`core/file_tools.py` currently implements `list_files` and `read_file`.

### list_files

- Uses `WorkspaceBoundary.open_file()`.
- Opens directories with `O_RDONLY | O_DIRECTORY | O_NONBLOCK`.
- Uses `os.scandir(fd)`.
- Non-recursive.
- Sorted names; hidden entries included.
- Symlink entry names may be listed, but the listing does not follow them.
- Default limit: 1,000 entries.
- Raises `TooManyEntriesError` when the limit is exceeded.

### read_file

- Uses `WorkspaceBoundary.open_file()`.
- Opens with non-blocking read flags.
- Requires a regular file after `fstat`.
- Default maximum: 1 MiB.
- Checks initial file size and reads bounded chunks to detect growth past the limit.
- Strict UTF-8 decoding.
- Rejects directories, invalid UTF-8, and FIFO files.

### Configuration and errors

- Limits are constructor-configurable.
- Boolean, non-integer, and non-positive limits are rejected.
- Public configuration properties are read-only.
- `WorkspaceViolation` propagates from the workspace boundary.
- Relevant `OSError` exceptions are wrapped in FileTools errors.

The implementation closes descriptors after operations, including error paths. The current test suite does not establish exhaustive behavior for every special file or every descriptor failure scenario.

## 11. Docker execution model

Docker Engine is installed inside Ubuntu on WSL2. The intended architecture is:

- Runner executes as a WSL host process.
- Docker runs project code and tests.
- The agent does not receive an unrestricted host terminal.
- Docker socket is never passed to an agent container.
- Network and secrets are disabled for the initial agent execution environment unless a future explicit policy says otherwise.
- Docker is an execution boundary, not the agent itself.

The user currently invokes Docker through `sudo docker`; the user is not in the Docker group. Changing that is a security-sensitive decision because Docker group access is highly privileged.

Docker Engine 29.9.2 and Compose 5.6.1 were present in the recorded environment. Docker's presence does not mean Runner test execution is already integrated.

## 12. Current implementation status

### Implemented and tested

- UUID-based identifiers.
- Run lifecycle data model and repair-cycle constraints.
- Operation data model.
- Three-stream TraceCollector.
- Permission levels, mapping, and policy methods.
- Linux `openat2` WorkspaceBoundary.
- Workspace boundary tests.
- `FileTools.list_files()`.
- `FileTools.read_file()`.
- FileTools tests.

The last reported full suite result on 2026-11-01 was **80 passed in 0.12s**. Re-run tests in the actual Runner checkout before treating this as current.

### Not implemented

- `write_file`.
- `apply_patch`.
- Agent-facing facade.
- Centralized tool dispatch.
- Permission enforcement around actual tool invocation.
- Automatic Operation lifecycle for tool calls.
- Automatic trace emission for each tool call.
- Docker test execution through Runner.
- Plan schema/validation and orchestration.
- End-to-end Run reporting.
- Model/provider adapter and LLM integration.
- Enforced network and secret isolation for a future model-connected agent.

### Known local Git snapshot

The local Runner repository was reported to have these commits:
- `479e681` — Initial Runner implementation with secure workspace boundary.
- `b26fd5c` — Document secure workspace access policy.
- `8942e4b` — Add development guide for Runner.

At the last reported inspection, `core/file_tools.py` and `tests/test_file_tools.py` were untracked, while `design.md` and `DEVELOPMENT_GUIDE.md` had local edits. No new commit was authorized. Confirm the actual local status before continuing.

## 13. Immediate next phase: write_file

Implement only `write_file` next. Do not combine it with `apply_patch`.

Requirements:
1. Create or replace files only within the configured workspace.
2. Use `WorkspaceBoundary.open_file()` or a rigorously reviewed descriptor-relative atomic replacement design that preserves the workspace boundary.
3. Choose flags and modes inside Runner code; never accept them from agent input.
4. Prefer atomic replacement.
5. A failed write must not leave an existing target partially overwritten.
6. Define behavior for existing symlinks, permissions, missing parent directories, and replacement.
7. Test path escapes, symlink attacks, permission errors, interrupted operations, and replacement edge cases.
8. Document the exact semantics and limitations.

After `write_file` is implemented, tested, and reviewed, update this design and the development guide. Only then plan `apply_patch` as a separate phase.

## 14. Open design questions

These items are not silently decided by the current implementation:

- What default global Run timeout should be used?
- Should Operation `result` and `error` be mutually exclusive, or may a failed operation retain partial result metadata?
- What exact atomic-replacement semantics should `write_file` guarantee for permissions, symlinks, and parent directories?
- How should trace writes handle concurrent writers if concurrency is introduced later?
- What structured schema should represent a Plan and its validation findings?
- What exact interface should the agent-facing facade expose without leaking mutable internal state?
- What policy should govern future network access, if it is ever enabled?

Resolve these questions explicitly before implementing the affected behavior.

## 15. Transfer and maintenance rules

This document is intended to become `design.md` in the local Runner repository.

- Read this file together with `DEVELOPMENT_GUIDE.md`.
- Verify source code and tests before treating a status as current.
- Update the design when architecture or a significant technical decision changes.
- Keep implementation status separate from planned capabilities.
- Do not commit or publish changes without explicit user approval.
- If code, tests, and documentation disagree, investigate the discrepancy and record only verified behavior.

**The design describes intended boundaries and current implementation separately. It does not override code, tests, security evidence, or explicit user decisions.**
