# Backend

FastAPI backend for OMGM.

## Setup

```bash
UV_CACHE_DIR=../.uv-cache uv sync --extra dev
```

## Run

```bash
UV_CACHE_DIR=../.uv-cache uv run uvicorn app.main:app --reload
```

Swagger opens at `http://localhost:8000/`.

Health Check:

```bash
curl http://localhost:8000/health
```

## Test

```bash
UV_CACHE_DIR=../.uv-cache uv run pytest
UV_CACHE_DIR=../.uv-cache uv run ruff check app tests
```

## Docker

From the repository root:

```bash
cp .env.example .env
docker compose up
```

Replace the placeholder `POSTGRES_PASSWORD` in `.env` before sharing or long-running local use.
