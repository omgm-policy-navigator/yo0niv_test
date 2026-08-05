# Backend Phase 1 Plan

## Goal

Build the backend project's basic executable runtime with FastAPI, uv, PostgreSQL configuration, Docker Compose, environment variables, health check, and setup documentation.

## In Scope

- `backend/app` FastAPI package.
- `backend/pyproject.toml` and `backend/uv.lock`.
- PostgreSQL `DATABASE_URL` settings.
- SQLAlchemy async engine object.
- Dockerfile and Docker Compose runtime.
- `/health` endpoint.
- Swagger at localhost root.
- Backend tests and lint.

## Out of Scope

- Business logic.
- Repository.
- ORM models.
- Alembic migrations.
- Business APIs.
- Authentication.
