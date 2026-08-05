# Development Process

## Phases

Track implementation by small phases in pull requests and ADRs when a decision affects boundaries or future migration cost.

1. Project foundation: runtime, health check, configuration, logging, tests, Docker Compose, documentation.
2. Domain vocabulary and question flow contracts.
3. Rule evaluation service using in-memory fixtures.
4. PostgreSQL schema, migrations, and repository ports.
5. Policy graph API and chatbot context payloads.
6. RAG document storage and retrieval using pgvector.
7. Notification and saved policy workflows.

## Documentation Rules

- Keep `README.md` as the entrypoint with commands and links only.
- Put architecture and ownership rules in `docs/architecture.md`.
- Put operational fixes in `docs/troubleshooting.md`.
- Record durable design decisions as ADRs in `docs/adr/`.
- Do not create placeholder documents for work that has not started.

## Code Rules

- Keep API handlers thin; use services for use-case orchestration.
- Keep domain vocabulary independent from FastAPI, databases, and LLM clients.
- Add infrastructure adapters only when a feature needs them.
- Prefer explicit types and small modules over broad utility layers.
- Update `backend/uv.lock` whenever backend dependencies change.

## Test Rules

- Add tests with each behavior change.
- Keep fixtures small, stable, and non-secret.
- Test public behavior first, then pure domain logic where useful.
- Do not require network or external services for default tests.
