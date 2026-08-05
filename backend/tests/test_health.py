from fastapi.testclient import TestClient

from app.main import create_app


def test_health_check_returns_runtime_status() -> None:
    client = TestClient(create_app())

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "app": "OMGM Backend",
        "environment": "local",
    }


def test_health_check_returns_request_id_header() -> None:
    client = TestClient(create_app())

    response = client.get("/health", headers={"x-request-id": "test-request-id"})

    assert response.status_code == 200
    assert response.headers["x-request-id"] == "test-request-id"


def test_database_health_check_returns_ok(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    async def healthy(_engine) -> bool:  # type: ignore[no-untyped-def]
        return True

    monkeypatch.setattr("app.api.health.check_database_health", healthy)

    with TestClient(create_app()) as client:
        response = client.get("/health/db")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_database_health_check_returns_unavailable(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    async def unhealthy(_engine) -> bool:  # type: ignore[no-untyped-def]
        return False

    monkeypatch.setattr("app.api.health.check_database_health", unhealthy)

    with TestClient(create_app()) as client:
        response = client.get("/health/db")

    assert response.status_code == 503
    assert response.json() == {"status": "unavailable"}
