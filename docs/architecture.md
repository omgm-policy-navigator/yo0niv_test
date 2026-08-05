# Architecture

## Current Scope

This repository owns the MVP backend service for Seoul newlywed policy navigation. It exposes FastAPI endpoints, loads runtime configuration, emits structured logs, and will coordinate policy question flows, rule-based pre-diagnosis, policy graph data, and RAG-backed explanations.

Frontend, data collection jobs, human review tooling, and production infrastructure are separate source boundaries. They should gain implementation files only when their ownership is concrete.

## Technology Stack

- Python 3.9 or newer
- FastAPI and Uvicorn for HTTP APIs
- Pydantic Settings for environment-based configuration
- structlog for JSON structured logs
- pytest and FastAPI TestClient for tests

Planned persistence is PostgreSQL with pgvector. Database clients, migrations, and vector search adapters should be added only when the first persistence-backed feature is implemented.

## Module Boundaries

- `backend/`: FastAPI backend source root.
- `backend/policy_navigator/main.py`: backend application factory and runtime entrypoint.
- `backend/policy_navigator/api/`: HTTP routes and request/response translation.
- `backend/policy_navigator/core/`: cross-cutting runtime concerns such as configuration and logging.
- `backend/policy_navigator/domain/`: backend-owned domain vocabulary and pure domain models.
- `backend/policy_navigator/services/`: use-case orchestration across domain logic and infrastructure ports.
- `frontend/`: React/Vite client boundary. No application code is added until frontend work begins.
- `infra/`: infrastructure boundary for Docker, compose, deployment, and local runtime assets.
- `tests/`: executable tests mirroring public behavior and stable domain vocabulary.
- `tests/resources/`: small non-secret test fixtures only.
- `docs/`: living documentation that is actually used by the team.

## Data Ownership

The backend owns normalized policy condition vocabulary, user facts, policy evaluation results, policy relation semantics, and API-facing graph data. Official policy source documents remain externally sourced evidence; the backend stores derived structured data and source references, but administrator review workflows are a separate ownership concern.

## Persistence Direction

The MVP data model is expected to begin with:

- `category`
- `policy`
- `policy_rule`
- `question`
- `user_fact`
- `policy_evaluation`
- `policy_relation`
- `policy_document`

`policy_document.embedding` should use pgvector when persistence is introduced. Avoid adding a separate vector database unless PostgreSQL becomes insufficient for observed retrieval scale.
