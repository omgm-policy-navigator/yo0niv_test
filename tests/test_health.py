from fastapi.testclient import TestClient
from policy_navigator.main import create_app


def test_health_check_returns_runtime_status() -> None:
    client = TestClient(create_app())

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "app": "Seoul Newlywed Policy Navigator",
        "environment": "local",
    }


def test_health_check_returns_request_id_header() -> None:
    client = TestClient(create_app())

    response = client.get("/health", headers={"x-request-id": "test-request-id"})

    assert response.status_code == 200
    assert response.headers["x-request-id"] == "test-request-id"
