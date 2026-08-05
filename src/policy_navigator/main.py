from fastapi import FastAPI

from policy_navigator.api.health import router as health_router
from policy_navigator.core.config import get_settings
from policy_navigator.core.logging import configure_logging


def create_app() -> FastAPI:
    settings = get_settings()
    configure_logging(settings.log_level)

    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        docs_url=f"{settings.api_prefix}/docs",
        openapi_url=f"{settings.api_prefix}/openapi.json",
    )
    app.include_router(health_router)
    return app


app = create_app()
