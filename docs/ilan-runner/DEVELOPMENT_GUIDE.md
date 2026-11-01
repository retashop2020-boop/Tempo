# Ilan Agent Runner — Development Guide

**Purpose:** A practical handover guide for continuing the Ilan Agent Runner in a separate local repository.

**Expected local project root:** `~/ilan-lab/runner/`

**Documentation snapshot:** 2026-11-01

**Current stage:** Core infrastructure and workspace-bounded read tools (`list_files`, `read_file`) are implemented. The read tools have passed the current full test suite. Write/patch tools, Runner orchestration, Docker-backed test execution through Runner, and model integration remain pending.

> This document is a handover snapshot. Verify the local repository, Git status, source files, and tests before relying on any status claim. The Tempo repository is only being used as a temporary transfer location for these two documentation files; it is not the Runner source repository.

---

## 1. Project purpose

Ilan Runner is a controlled local execution environment for a future autonomous software-development agent.

The intended agent workflow is to inspect a project, prepare a plan, request bounded file changes, run permitted tests, analyze actual results, and attempt a limited number of repairs.

The Runner—not the agent—must control:
- Workspace boundaries.
- Tool authorization.
- Operation records.
- Trace collection.
- Test execution boundaries.
- Run lifecycle and stopping conditions.

The first version is a local CLI application. It is deliberately independent of any particular model, provider, UI, or agent personality. Model integration comes later.

### Roles

| Component | Responsibility |
|---|---|
| User | Defines goals, permissions, budgets, and approval boundaries |
| Ilan 🚀 | Development agent; plans and requests actions within granted capabilities |
| Igor 🧠 | Tracks decisions, implementation state, documentation, and consistency |
| Runner | Enforces boundaries, invokes tools, records evidence, and controls lifecycle |
| Docker | Provides an isolated execution environment for project code and tests |

Docker is an execution environment, not an autonomous agent.

## 2. Non-negotiable operating principles

**The agent may decide what to request; the Runner decides what is allowed and what actually happens.**

- Independence in problem-solving does not imply independence in defining authority.
- The agent must not grant or expand its own permissions.
- The agent must not obtain unrestricted host-terminal access.
- The agent must not directly access Runner configuration, logs, or traces.
- The agent must not access secrets or API credentials in v1.
- The agent must not receive the Docker socket.
- The agent must not change execution limits.
- The agent must not commit, push, merge, publish, purchase, or incur costs.
- The agent's claim that an action succeeded is not evidence that it succeeded.
- Completion must be determined from Runner-controlled execution and test evidence.
- Default Deny and Least Privilege apply.
- A permission to write does not imply permission to execute.

The user retains control over consequential actions, including Git publication and any financial commitment.

## 3. Current repository structure

The expected Runner repository structure at this snapshot is:

```text
runner/
├── .git/
├── .gitignore
├── __init__.py
├── design.md
├── DEVELOPMENT_GUIDE.md
├── main.py
├── core/
│   ├── __init__.py
│   ├── ids.py
│   ├── run.py
│   ├── operation.py
│   ├── trace.py
│   ├── permissions.py
│   ├── workspace.py
│   └── file_tools.py
└── tests/
    ├── __init__.py
    ├── test_ids.py
    ├── test_run.py
    ├── test_operation.py
    ├── test_trace.py
    ├── test_permissions.py
    ├── test_workspace.py
    └── test_file_tools.py
```

The list above reflects the implementation snapshot reported on 2026-11-01. Confirm it against the actual checkout before making changes.

### Module responsibilities

| Module | Responsibility |
|---|---|
| `core/ids.py` | Generates unique run, request, and operation identifiers |
| `core/run.py` | Tracks Run lifecycle and repair-cycle limits |
| `core/operation.py` | Represents one tool operation and its result/error |
| `core/trace.py` | Appends structured evidence to JSONL trace streams |
| `core/permissions.py` | Defines permission levels, tool mapping, and policy methods |
| `core/workspace.py` | Enforces workspace-bounded filesystem access using Linux `openat2` |
| `core/file_tools.py` | Implements the current workspace-bounded read tools |
| `main.py` | Intended CLI entry point; currently empty |
| `tests/` | Automated tests for core components and FileTools |

## 4. Run, Request, and Operation

These concepts have separate identities and lifecycles.

### Run

A Run represents one complete development task. The Runner generates its `run_id`.

Run statuses:
- `running` — internal active state.
- `completed` — success criteria are supported by evidence.
- `failed` — permitted repair cycles were exhausted while tests still fail.
- `timeout`
- `cancelled`
- `blocked`
- `inconclusive` — tests may pass, but the requested goal has not been established.

The maximum is **three repair cycles after the initial failed test**, for at most four test executions in one Run. The Runner must enforce this limit; the agent cannot extend it.

A Run is not complete merely because the agent says it is complete.

### Request

A Request represents the agent's main task request within a Run. Multiple Operations may belong to one Request. The Runner generates `request_id`.

### Operation

An Operation represents one specific tool invocation. The Runner generates a new `operation_id` for every invocation, including repeated calls with identical inputs.

Expected fields:
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

Operation statuses:
- `success`
- `error`
- `denied`
- `timeout`
- `cancelled`

Operation status and Run status must never be conflated. Use `parent_operation_id` only when an operation is genuinely dependent on another operation.

## 5. Permission model

Three permission levels are defined:

| Permission | Meaning |
|---|---|
| `READ` | Inspect files and permitted project state |
| `WRITE` | Create or modify project files |
| `EXECUTE` | Run explicitly permitted commands or tests |

The current mapping in `core/permissions.py` includes:

| Tool | Permission | Current implementation |
|---|---|---|
| `list_files` | READ | Implemented |
| `read_file` | READ | Implemented |
| `git_status` | READ | Planned |
| `git_diff` | READ | Planned |
| `write_file` | WRITE | Planned |
| `apply_patch` | WRITE | Planned |
| `run_tests` | EXECUTE | Planned |

The permission mapping does not mean that every listed tool already exists. Verify the tool implementation separately.

The current `PermissionPolicy` has `authorize()`, `grant()`, and `revoke()` methods. Grant/revoke must remain under administrative Runner control. The agent-facing interface must not expose those methods.

The three permission levels are an authorization model, not a substitute for safe implementation of each tool.

## 6. Workspace security

The intended project workspace used for the current development tests is:

```text
~/ilan-lab/workspace/sample-project
```

The agent must not directly access Runner configuration, logs, or traces, including:

```text
~/ilan-lab/configs
~/ilan-lab/logs
~/ilan-lab/traces
```

The agent must not receive unrestricted access to the rest of the user's home directory, network resources, or secrets.

### WorkspaceBoundary

`core/workspace.py` implements a Linux `openat2`-based filesystem boundary.

The implementation:
- Opens the configured workspace root and retains its directory file descriptor.
- Resolves actual file access relative to that descriptor.
- Uses `RESOLVE_BENEATH` to prevent path resolution from escaping the workspace.
- Uses `RESOLVE_NO_MAGICLINKS` to reject magic-link traversal.
- Allows relative symbolic links only when resolution remains beneath the workspace root.
- Rejects absolute symbolic links.
- Rejects absolute user-supplied paths and parent-directory traversal.

`resolve()` is for validation/inspection; it is not a safe substitute for the actual open operation. File tools must use `WorkspaceBoundary.open_file()` for filesystem access.

The implementation depends on Linux `openat2` support. It was tested in WSL2 on x86_64 with kernel 6.18.54.1.

### Security limitations

This is a workspace-bounded path-resolution mechanism, not a complete filesystem security boundary.

- Hard links are not restricted by `openat2` path resolution.
- The configured workspace root is trusted when initialized.
- The caller of `open_file()` supplies flags; in the eventual agent-facing system, only Runner-controlled code may choose those flags.
- `resolve()` alone is subject to the usual gap between checking a path and later using it; actual access must go through the descriptor-based open operation.
- Special device files may have open-time effects before a later file-type check. Do not claim that all special-file side effects are prevented.
- Docker isolation is not an absolute security guarantee.

## 7. FileTools — current implementation

Module: `core/file_tools.py`

The current implementation contains two read tools:
- `list_files`
- `read_file`

Both use `WorkspaceBoundary.open_file()` for actual filesystem access. They do not use ordinary path-based opening as a bypass around the workspace boundary.

### `list_files`

- Lists only the direct entries of the requested directory; it is non-recursive.
- Uses a directory file descriptor and `os.scandir(fd)`.
- Returns sorted entry names, including hidden names.
- Does not follow listed symlink entries.
- Default maximum: 1,000 entries.
- Raises `TooManyEntriesError` when the configured limit is exceeded.
- Uses non-blocking open flags and closes the directory descriptor after the operation.

### `read_file`

- Accepts regular files only.
- Uses non-blocking open flags.
- Default maximum size: 1 MiB (1,048,576 bytes).
- Checks the initial size and reads bounded chunks, allowing it to detect growth beyond the configured limit.
- Decodes text as strict UTF-8.
- Rejects directories, invalid UTF-8, and FIFO files.
- Closes the file descriptor after the operation, including error paths.

### Configuration and error behavior

- Read and listing limits are configurable through the FileTools constructor.
- Boolean, non-integer, and non-positive limits are rejected.
- `WorkspaceViolation` from the workspace boundary propagates.
- Relevant filesystem `OSError` exceptions are wrapped as FileTools errors.

### Current tests

The FileTools test module covers:
- Sorted direct entries, hidden entries, non-recursive listing, and relative directories.
- Default and custom entry limits.
- Symlink escape attempts for listing and reading.
- UTF-8 content, exact size limits, oversized files, and custom read limits.
- Directory rejection and invalid UTF-8.
- FIFO rejection without blocking.
- Invalid configuration values and read-only public configuration properties.

The current full suite result reported on 2026-11-01 is **80 passed**. Re-run tests in the actual local checkout before treating this as the latest result. Not every implementation detail has a dedicated test; in particular, do not imply that descriptor closure or special-device behavior has been exhaustively tested.

## 8. Trace architecture

Each Run is intended to have its own trace directory:

```text
traces/
└── <run_id>/
    ├── agent_trace.jsonl
    ├── execution_trace.jsonl
    └── test_trace.jsonl
```

### Agent Trace

Records agent decisions and requests:
- Plans.
- Assumptions.
- Requested tools.
- Reasons for choices.

It answers: **Why did the agent request this action?**

### Execution Trace

Records what the Runner actually did:
- Tool invocation.
- Operation identifiers.
- Start and finish times.
- Success/failure.
- Permission denials.
- Exceptions.
- Execution output or error information.

It answers: **What actually happened?**

### Test Trace

Records:
- Test execution.
- Test results.
- Assertion failures.
- Relevant test artifacts.

It answers: **What did the tests establish?**

All streams use shared identifiers where relevant. An agent explanation is not a substitute for evidence from the Runner.

Trace levels:
- `minimal`
- `normal` — default
- `debug`

The user or Runner configuration controls the level. The agent must not lower it or delete/modify existing traces.

Current limitation: TraceCollector appends JSONL records and flushes writes. It is not tamper-proof and does not guarantee durability against sudden power loss.

## 9. Intended Runner orchestration

The planned lifecycle is:

1. Runner generates `run_id` and initializes the Run.
2. Agent receives the task.
3. Agent inspects workspace context through READ tools.
4. Agent submits a structured Plan containing goal, target files, steps, assumptions, risks, and success criteria.
5. Runner records and validates the Plan. A Plan does not grant permissions.
6. Agent requests a tool operation.
7. Runner creates an Operation and checks authorization.
8. Runner invokes the relevant tool.
9. Runner records the actual result or error.
10. Tests run in Docker through an explicitly permitted execution path.
11. Test results are recorded in Test Trace.
12. Agent analyzes the evidence.
13. If tests fail, the agent may repair and retry within the repair-cycle limit.
14. Runner determines the final Run status from evidence and lifecycle rules.
15. Runner produces a final report.

The agent must not receive direct mutable access to internal Run state, administrative permission methods, TraceCollector internals, or raw FileTools objects. An agent-facing facade should expose only the permitted operations.

### Repair policy

- Initial test execution may fail.
- Up to three repair cycles are allowed.
- Maximum test executions per Run: four.
- The Runner enforces the limit.
- The agent cannot extend the limit.
- Tests passing without evidence that the requested goal was achieved must result in `inconclusive`, not automatic `completed`.

### Not implemented yet

The orchestration flow above is a design target, not a claim about current runtime behavior. The Runner does not yet automatically connect tool calls to authorization, Operation creation, Trace recording, Docker test execution, or model requests.

## 10. Docker and execution isolation

Docker Engine is installed inside Ubuntu on WSL2.

Intended model:
- Runner executes as a WSL host process.
- Docker runs project code and tests.
- The agent does not receive unrestricted host-terminal access.
- The Docker socket is never mounted into an agent container.
- The agent cannot use Docker to obtain broader host privileges.
- Network and secrets remain unavailable to the agent in the initial version.

Docker Engine is currently used through `sudo docker`. The user has not been added to the `docker` group. Do not change this without reviewing the security implications: membership in the Docker group is effectively highly privileged.

Docker is an execution isolation layer, not an autonomous agent and not an absolute security boundary.

## 11. Development workflow

For every meaningful change:

1. **Inspect:** Read the relevant implementation and tests. Do not assume a feature exists because it appears in the design.
2. **Define:** State the module, responsibility, compatibility requirements, security properties, and tests.
3. **Implement incrementally:** Keep filesystem logic, permission enforcement, Run lifecycle, Trace recording, and model/provider logic separate.
4. **Test:** Run focused tests first, then the full suite.
5. **Inspect the diff:** Check unexpected files, unintended changes, security regressions, and overstated documentation.
6. **Update docs:** Update `design.md` when a design decision or significant technical detail changes. Update this guide when architecture, implementation status, a phase, or the next step changes.
7. **Commit only with user approval:** Never commit, push, merge, or publish without explicit approval. Use specific file paths rather than broad `git add .`.

Current full-suite command:

```bash
pytest -q ~/ilan-lab/runner/tests
```

Useful review commands:

```bash
git -C ~/ilan-lab/runner status --short
git -C ~/ilan-lab/runner diff --check
GIT_PAGER=cat git -C ~/ilan-lab/runner diff
```

## 12. Development environment

Known environment at the time of this snapshot:

- Windows 10 Pro 22H2, build 19045.6456.
- WSL2 with Ubuntu 22.04.1 LTS.
- Linux kernel 6.18.54.1.
- Docker Engine 29.9.2.
- Docker Compose 5.6.1.
- Python 3.10.12.
- Git 2.34.1 in WSL.
- pytest 9.2.0 in the project virtual environment.

The local sample project is:

```text
~/ilan-lab/workspace/sample-project
```

It contains a small Python application and pytest tests.

## 13. Local Git and implementation history

The Runner repository is local and independent from the Tempo repository.

Known local commits:
- `479e681 Initial Runner implementation with secure workspace boundary`
- `b26fd5c Document secure workspace access policy`
- `8942e4b Add development guide for Runner`

At the latest reported inspection:
- `core/file_tools.py` and `tests/test_file_tools.py` were untracked.
- `design.md` and `DEVELOPMENT_GUIDE.md` had local documentation changes.
- No new commit had been authorized or created for those changes.
- The last full test run reported 80 passing tests.

The exact current Git state must be checked locally. This snapshot must not be interpreted as proof that the working tree is still in the same state.

## 14. Current status and next development step

### Implemented

- Core identifier generation.
- Run lifecycle and repair-cycle limits.
- Operation data model.
- Three-stream TraceCollector.
- Permission levels, tool mapping, and policy methods.
- Initial Linux `openat2` WorkspaceBoundary.
- Workspace security tests.
- `FileTools.list_files()`.
- `FileTools.read_file()`.
- FileTools tests.
- Initial design and development documentation.

### Not implemented

- `write_file`.
- `apply_patch`.
- Agent-facing Runner facade.
- Actual permission enforcement around tool invocation.
- Automatic Operation creation and completion around tool calls.
- Automatic Trace creation for tool calls.
- Docker test execution through Runner.
- Structured Plan validation in the Runner.
- End-to-end orchestration and final report generation.
- Model/provider adapter and LLM integration.
- Network and secret isolation enforcement for a future model-connected agent.

### Immediate next task: implement only `write_file`

Do not start `apply_patch` in the same change.

Requirements to settle and implement:
- Create or replace files only within the configured workspace.
- Use `WorkspaceBoundary.open_file()` or a carefully designed descriptor-relative atomic-replacement flow that preserves the workspace boundary.
- File-opening flags and modes must be controlled by Runner code, never supplied by agent input.
- Prefer atomic replacement.
- A failed write must not leave an existing target partially overwritten.
- Define behavior for existing symlinks, file permissions, parent directories, and replacement.
- Test workspace escapes, symlink attacks, permission errors, failure/interruption behavior, and relevant replacement edge cases.
- Keep the implementation small and review its security assumptions before proceeding.

After `write_file` is implemented, tested, reviewed, and documented, plan `apply_patch` as a separate phase. Only after the file tools are stable should the project proceed to Runner orchestration.

## 15. Starting a new development conversation

At the start of a new conversation:

1. Read `DEVELOPMENT_GUIDE.md` and `design.md` from the actual local Runner repository.
2. Inspect `git status --short` and the latest commit.
3. Inspect the actual implementation and tests; do not rely exclusively on this guide.
4. Compare the code, tests, and documentation.
5. Confirm the immediate next task with the user before making architectural changes.
6. Work in small steps and request terminal output when the result affects the next decision.
7. Do not commit or publish without explicit user approval.

**This guide is a navigation and handover document. It does not override source code, tests, security evidence, or explicit user decisions. If the code contradicts this guide, investigate first and document only verified behavior.**
