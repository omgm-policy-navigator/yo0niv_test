import pytest
from pydantic import ValidationError

from app.core.config import Settings


def test_settings_accept_known_environment_values() -> None:
    settings = Settings(
        app_env="production",
        log_level="ERROR",
        database_url="postgresql+asyncpg://user:pass@localhost:5432/omgm",
    )

    assert settings.app_env == "production"
    assert settings.log_level == "ERROR"
    assert settings.sqlalchemy_database_url == "postgresql+asyncpg://user:pass@localhost:5432/omgm"


def test_settings_reject_invalid_environment_values() -> None:
    with pytest.raises(ValidationError):
        Settings(app_env="prod", log_level="NOPE", database_url="not-a-url")


def test_settings_require_database_url(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    monkeypatch.delenv("DATABASE_URL", raising=False)

    with pytest.raises(ValidationError):
        Settings(_env_file=None)
