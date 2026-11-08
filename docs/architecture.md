# Architecture and threat model

CLI parses local paths -> analyzer invokes `python -m ruff` and optionally `python -m pytest` -> reporter serializes structured results. Tooling runs in subprocesses with `shell=False` and bounded runtime. No network operations are implemented by CodeProof itself, but invoked tooling/plugins may perform network activity.

## Trust boundary

All target repositories must be trusted. Pytest executes code; Ruff and its configuration/dependencies must also be treated as software supply-chain inputs. Do not advertise this as a secure sandbox.

## Future engineering backlog

1. Add JSON Schema validation and normalized finding IDs.
2. Add fixtures and integration tests using isolated temporary projects.
3. Implement output truncation limits and more structured tool errors.
4. Add configurable rules and baselines.
5. Explore isolated execution in a disposable environment with explicit threat modeling.
6. Add release versioning, provenance, and pinned CI actions.
