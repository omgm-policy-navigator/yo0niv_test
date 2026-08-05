# Backend Phase 1 Port Conflict

## Symptom

`curl http://127.0.0.1:8000/health` may return an unexpected response when another local development server already owns port 8000.

`docker compose up` may also fail when another local PostgreSQL already owns host port 5432.

## Diagnosis

```bash
lsof -nP -iTCP:8000 -sTCP:LISTEN
lsof -nP -iTCP:5432 -sTCP:LISTEN
docker compose port backend 8000
docker compose logs --tail=80 backend
```

## Resolution

Stop the unrelated local process or verify the backend inside the container:

```bash
docker compose exec backend python -c "import urllib.request; r=urllib.request.urlopen('http://127.0.0.1:8000/health'); print(r.status); print(r.read().decode())"
```

This project maps local PostgreSQL to host port `5433` by default while containers still use `postgres:5432`.

If backend host port 8000 is occupied, set `BACKEND_PORT=8001` in local `.env` and use `http://localhost:8001/` for that local session. The container still listens on port 8000.
