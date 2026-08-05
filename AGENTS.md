# AGENTS.md

## Repository Purpose

This repository is the FastAPI backend for the Seoul newlywed policy navigator. It owns backend APIs, policy condition vocabulary, rule-evaluation orchestration, RAG service boundaries, runtime configuration, structured logging, and backend tests.

## Architecture Rules

- `backend/app/main.py` is the backend application factory and runtime entrypoint.
- `backend/app/api/` contains HTTP routes only. Keep handlers thin and delegate use-case work to services.
- `backend/app/core/` contains cross-cutting runtime concerns such as settings, lifespan, logging, and request context.
- `backend/app/db/` contains database connection objects. Do not add ORM models or repositories before their phase.
- `backend/app/models/` is reserved for SQLAlchemy models in a later phase.
- `backend/app/schemas/` contains API response/request schemas. Entity and API schemas must stay separate once entities exist.
- `backend/app/services/` coordinates use cases and may depend on domain models and explicit infrastructure boundaries once those exist.
- `frontend/` is reserved for the React/Vite client once frontend implementation begins.
- `infra/` is reserved for local/runtime infrastructure assets such as Docker, compose files, and deployment configuration once those are introduced.
- `tests/` mirrors behavior that must keep working. Use `tests/resources/` only for small, non-secret fixtures.
- `docs/` contains living documents only. Do not create empty placeholder docs.

## Code Standards

- Target Python 3.11.
- Manage backend dependencies in `backend/pyproject.toml` with `uv`.
- Keep resolved backend dependency versions in `backend/uv.lock`.
- Keep `.venv/` local and untracked.
- Prefer explicit domain names over generic utilities.
- Add an abstraction only when a concrete feature needs it.
- Keep configuration environment-driven through `pydantic-settings`.
- Emit structured JSON logs through `structlog`.

## Test Standards

- Default tests must run without network, database, LLM, or vector-store access.
- Add or update tests with every behavior change.
- Keep test fixtures deterministic and free of secrets.
- Run `pytest` before handing off changes.

## Documentation Standards

- Keep `README.md` short: purpose, setup, execution, test commands, and links.
- Put architecture and ownership details in `docs/architecture.md`.
- Put phase tracking and contribution rules in `docs/development-process.md`.
- Put operational fixes in `docs/troubleshooting.md`.
- Put durable decisions in `docs/adr/`.

## Git Hygiene

- Do not commit secrets, `.env`, `.venv`, logs, local data, cache directories, or build artifacts.
- Avoid reverting unrelated user changes.
- Keep commits focused on the requested work.
