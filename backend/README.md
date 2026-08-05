# Backend

FastAPI backend source root.

Current responsibilities:

- HTTP API entrypoint
- Health Check
- Runtime configuration
- Structured logging
- Backend-owned policy vocabulary
- Backend tests

Run from the repository root:

```bash
uvicorn policy_navigator.main:app --reload
```
