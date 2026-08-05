# Seoul Newlywed Policy Navigator

서울 생활권 예비·신혼부부가 주거, 대출, 웨딩, 세제, 출산·육아 정책의 자격 조건과 신청 순서를 판단할 수 있도록 돕는 정책 내비게이션 백엔드입니다.

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install ".[dev]"
cp .env.example .env
uvicorn policy_navigator.main:app --reload
```

Health check:

```bash
curl http://127.0.0.1:8000/health
```

Tests:

```bash
pytest
```

## Documentation

- [Idea Design](docs/idea-design.md)
- [User Scenarios](docs/user-scenarios.md)
- [Functional Requirements](docs/functional-requirements.md)
- [Data Design](docs/data-design.md)
- [System Architecture](docs/system-architecture.md)
- [Architecture](docs/architecture.md)
- [Development Process](docs/development-process.md)
- [Troubleshooting](docs/troubleshooting.md)
- [ADR Index](docs/adr/README.md)

## Repository Responsibility

This repository owns the FastAPI backend API, rule-based policy pre-diagnosis boundary, RAG service boundary, runtime configuration, logging, and backend tests. Frontend UI, source data approval workflows, and production infrastructure can be added as separate modules or repositories when their ownership becomes concrete.
