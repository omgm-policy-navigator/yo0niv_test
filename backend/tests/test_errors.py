from fastapi.testclient import TestClient

from app.main import create_app


def test_not_found_error_includes_request_id() -> None:
    client = TestClient(create_app())

    response = client.get("/missing", headers={"x-request-id": "missing-route"})

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Not Found",
        "request_id": "missing-route",
    }
