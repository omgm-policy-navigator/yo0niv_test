from sqlalchemy.ext.asyncio import AsyncEngine

from app.core.config import Settings
from app.db.connection import create_database_engine
from app.main import create_app


def test_create_database_engine_uses_configured_database_url() -> None:
    settings = Settings(database_url="postgresql+asyncpg://user:pass@localhost:5432/omgm")

    engine = create_database_engine(settings)

    assert isinstance(engine, AsyncEngine)
    assert "localhost" in str(engine.url)


def test_lifespan_disposes_database_engine(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    disposed = False

    class FakeEngine:
        async def dispose(self) -> None:
            nonlocal disposed
            disposed = True

    monkeypatch.setattr("app.core.lifespan.create_database_engine", lambda _settings: FakeEngine())

    from fastapi.testclient import TestClient

    with TestClient(create_app()):
        pass

    assert disposed is True
