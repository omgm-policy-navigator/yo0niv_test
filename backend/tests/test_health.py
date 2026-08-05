from fastapi.testclient import TestClient

from app.core.config import get_settings
from app.main import create_app


def test_health_check_returns_runtime_status(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    monkeypatch.setenv("APP_NAME", "OMGM Backend")
    get_settings.cache_clear()
    client = TestClient(create_app())

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "app": "OMGM Backend",
        "environment": "local",
    }


def test_health_check_returns_request_id_header(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    monkeypatch.setenv("APP_NAME", "OMGM Backend")
    get_settings.cache_clear()
    client = TestClient(create_app())

    response = client.get("/health", headers={"x-request-id": "test-request-id"})

    assert response.status_code == 200
    assert response.headers["x-request-id"] == "test-request-id"
