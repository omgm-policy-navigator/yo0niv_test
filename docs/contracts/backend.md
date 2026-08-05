# Backend Contract

## Phase 1 Runtime Contract

- Python version: 3.11
- Package manager: `uv`
- Project file: `backend/pyproject.toml`
- Lockfile: `backend/uv.lock`
- ASGI app: `app.main:app`
- Local command: `cd backend && UV_CACHE_DIR=../.uv-cache uv run uvicorn app.main:app --reload`
- Docker command: `docker compose up`
- Swagger URL: `http://localhost:8000/`
- Health endpoint: `GET /health`

## Environment Variables

| Name | Required | Default | Purpose |
| --- | --- | --- | --- |
| `APP_NAME` | No | `OMGM Backend` | FastAPI app title. |
| `APP_ENV` | No | `local` | Runtime environment label. |
| `LOG_LEVEL` | No | `INFO` | Backend log level. |
| `BACKEND_PORT` | No | `8000` | Host port mapped to backend container port 8000. |
| `DATABASE_URL` | Yes in Docker | local PostgreSQL URL | Async SQLAlchemy PostgreSQL URL. |
| `POSTGRES_DB` | No | `omgm` | Local PostgreSQL database name. |
| `POSTGRES_USER` | No | `omgm` | Local PostgreSQL user. |
| `POSTGRES_PASSWORD` | Yes in Docker | none | Local PostgreSQL password. |
| `POSTGRES_PORT` | No | `5433` | Host port mapped to container PostgreSQL 5432. |

## Current API

```http
GET /health
GET /health/db
```

Response:

```json
{
  "status": "ok",
  "app": "OMGM Backend",
  "environment": "local"
}
```

`GET /health/db` executes `SELECT 1` through the app-managed async SQLAlchemy engine and returns:

```json
{
  "status": "ok"
}
```

Phase 1 does not introduce business APIs, authentication, repositories, ORM models, or migrations.
