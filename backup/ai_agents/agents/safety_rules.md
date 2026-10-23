# Safety Rules for Crash Prevention and Self-Protection

## Objective
The system must never enter a state where it causes instability, repeated crashes, or uncontrolled failure loops. If risk is detected, the system must protect itself first, then ask the agents to degrade gracefully instead of continuing unsafe execution.

## Core principles

### 1. Fail-safe before fail-fast
If the system sees signs of instability, it must pause risky operations before continuing.

### 2. Protect the process before the task
The system must prioritize its own health and stability over the completion of one operation.

### 3. Graceful degradation
When risk is high, the system should fall back to safe mode rather than crash.

### 4. Recover without losing state
Important data, session memory, and last known good state must be preserved before shutdown or reset.

### 5. Human-safe and agent-safe operation
No single agent is allowed to continue unsafe behavior alone. The safety cluster coordinates the response.

## Protective team

- VHOTIEX — central command and final decision maker
- AEGIS — security, risk, and policy review
- REX — validation, error handling, and recovery
- PULSE — monitoring, health checks, and alerts
- FORGE — safe code execution and rollback-safe implementation

## Safety rules

### Rule 1: Risk threshold guard
If any of the following crosses a defined threshold, the system must trigger safe mode:
- repeated exceptions in a short time window
- high memory pressure
- CPU saturation
- UI freeze or deadlock indicators
- unhandled network timeouts
- invalid state loops
- repeated retries with no progress

### Rule 2: Protect before continue
When risk is detected:
1. pause non-essential actions
2. stop retries that are compounding the failure
3. isolate the failing component
4. save the system state
5. route to safe recovery mode

### Rule 3: Safe mode requires minimal operation
In safe mode, the system must:
- disable risky background processes
- stop autonomous execution loops
- keep essential monitoring active
- reduce UI load
- show a restrained user message instead of crashing

### Rule 4: Recovery state must be preserved
Before any reset or restart, the app must:
- store recent session state
- save last known good configuration
- capture the exception context
- keep a minimal snapshot for diagnostics

### Rule 5: No infinite retry loop
If a task fails repeatedly, the system must stop retrying and escalate to a recovery workflow instead of looping forever.

### Rule 6: Self-protection override
Any agent that detects unstable conditions may trigger a protection event even if the main task is still in progress.

### Rule 7: Recovery is prioritized over completion
If a crash risk is real, the system should prefer a safe partial success over a full crash.

### Rule 8: Observability is mandatory
Every protection event must log:
- trigger type
- severity
- affected component
- recovery action
- time of event

## Emergency response flow

1. Detect anomaly
2. Measure risk severity
3. Trigger protection protocol
4. Halt unsafe execution
5. Save state and logs
6. Isolate failing component
7. Route to safe recovery path
8. Re-enable only after health check passes

## Example runtime policy

```python
if repeated_errors > 3 and memory_pressure > 0.85:
    trigger_safe_mode()
    stop_background_workflows()
    save_last_known_good_state()
    notify_pulse()
    ask_vhotiex_to_route_recovery()
```

## Final principle
The app must treat stability as a first-class feature. No feature, agent, or workflow is more important than protecting the app from crashing and preserving user trust.
