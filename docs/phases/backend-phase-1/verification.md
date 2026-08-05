# Backend Phase 1 Verification

## Local Backend

| Item | Command | Result | Notes |
| --- | --- | --- | --- |
| uv lock | `cd backend && UV_CACHE_DIR=../.uv-cache uv lock` | Passed | Python 3.11 lock generated |
| uv sync | `cd backend && UV_CACHE_DIR=../.uv-cache uv sync --extra dev --frozen` | Passed | `backend/.venv` ignored |
| pytest | `cd backend && UV_CACHE_DIR=../.uv-cache uv run pytest` | Passed | 6 passed, 1 Starlette/httpx deprecation warning |
| ruff | `cd backend && UV_CACHE_DIR=../.uv-cache uv run ruff check app tests` | Passed | All checks passed |
| uvicorn | `cd backend && UV_CACHE_DIR=../.uv-cache uv run uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload` | Passed | App started |
| health | `curl -i http://127.0.0.1:8000/health` | Passed | 200 OK |
| swagger | `curl -I http://127.0.0.1:8000/` | Passed | 200 OK, `text/html` |

## Docker Compose

| Item | Command | Result | Notes |
| --- | --- | --- | --- |
| compose config | `docker compose config --quiet` | Passed | Config parsed |
| backend build | `docker compose build backend` | Passed | uv-based backend image built |
| compose pytest | `docker compose run --rm backend pytest` | Passed | 6 passed, 1 Starlette/httpx deprecation warning |
| compose ruff | `docker compose run --rm backend ruff check app tests` | Passed | All checks passed |
| compose up | `docker compose up --build -d` | Passed | Verified with local `BACKEND_PORT=8001` because host 8000 was occupied |
| compose health | `curl -i http://127.0.0.1:8001/health` | Passed | 200 OK |
| compose swagger | `curl -I http://127.0.0.1:8001/` | Passed | 200 OK, `text/html` |

## Repository

| Item | Command | Result |
| --- | --- | --- |
| whitespace | `git diff --check` | Passed |
| ignored local files | `git status --short --ignored` | Passed. `.env`, `.uv-cache/`, `.venv/`, caches ignored |

## Migration

Alembic migration is not present in this repository and Phase 1 intentionally does not introduce ORM models or migrations.

## Known Limitations

- Host port 8000 was occupied in the local machine during verification. The committed default remains `BACKEND_PORT=8000`; local `.env` can override it.
- Business logic, repositories, ORM models, business APIs, and authentication are intentionally excluded.
