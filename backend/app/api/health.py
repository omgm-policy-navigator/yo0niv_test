from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

from app.core.config import get_settings
from app.db.health import check_database_health
from app.schemas.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    settings = get_settings()
    return HealthResponse(status="ok", app=settings.app_name, environment=settings.app_env)


@router.get("/health/db")
async def database_health_check(request: Request) -> JSONResponse:
    is_healthy = await check_database_health(request.app.state.db_engine)
    response_status = status.HTTP_200_OK if is_healthy else status.HTTP_503_SERVICE_UNAVAILABLE
    return JSONResponse(
        status_code=response_status,
        content={"status": "ok" if is_healthy else "unavailable"},
    )
