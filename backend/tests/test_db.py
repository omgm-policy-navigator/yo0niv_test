from sqlalchemy.ext.asyncio import AsyncEngine

from app.core.config import Settings
from app.db.connection import create_database_engine


def test_create_database_engine_uses_configured_database_url() -> None:
    settings = Settings(database_url="postgresql+asyncpg://user:pass@localhost:5432/omgm")

    engine = create_database_engine(settings)

    assert isinstance(engine, AsyncEngine)
    assert "localhost" in str(engine.url)
