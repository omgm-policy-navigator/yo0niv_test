import pytest

from app.core.config import get_settings


@pytest.fixture(autouse=True)
def isolate_settings(monkeypatch):  # type: ignore[no-untyped-def]
    monkeypatch.setenv("APP_NAME", "OMGM Backend")
    monkeypatch.setenv("APP_ENV", "local")
    monkeypatch.setenv("LOG_LEVEL", "INFO")
    monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://test:test@localhost:5432/test")
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()
