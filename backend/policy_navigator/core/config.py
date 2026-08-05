from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Seoul Newlywed Policy Navigator"
    app_env: str = "local"
    log_level: str = "INFO"
    api_prefix: str = Field(default="/api/v1", pattern=r"^/")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    return Settings()
