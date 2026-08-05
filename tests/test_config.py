import pytest
from policy_navigator.core.config import Settings
from pydantic import ValidationError


def test_settings_accept_known_environment_values() -> None:
    settings = Settings(app_env="production", log_level="ERROR", api_prefix="/api")

    assert settings.app_env == "production"
    assert settings.log_level == "ERROR"
    assert settings.api_prefix == "/api"


def test_settings_reject_invalid_environment_values() -> None:
    with pytest.raises(ValidationError):
        Settings(app_env="prod", log_level="NOPE", api_prefix="api")
