# 0001 Backend Foundation

Status: Accepted

Date: 2026-08-05

## Context

The MVP needs an executable backend foundation for policy question flows, rule-based pre-diagnosis, policy graph data, and RAG-backed policy explanations. The repository currently has no established implementation beyond an initial README.

## Decision

Use Python 3.9 or newer with FastAPI, Pydantic Settings, structlog, and pytest. Keep the first structure small:

- `api` for HTTP routes
- `core` for runtime configuration and logging
- `domain` for backend-owned vocabulary and pure models
- `services` for use-case orchestration

Do not add database, migration, LLM, or vector-search packages until the first feature needs those adapters.

## Consequences

The app can run and be tested immediately while leaving persistence and RAG integration decisions reversible. The module boundaries are explicit enough for the next phase without creating unused layers.
