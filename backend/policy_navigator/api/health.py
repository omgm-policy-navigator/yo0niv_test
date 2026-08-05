from fastapi import APIRouter

from policy_navigator.core.config import get_settings
from policy_navigator.domain.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    settings = get_settings()
    return HealthResponse(status="ok", app=settings.app_name, environment=settings.app_env)
