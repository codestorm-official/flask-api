"""Smoke tests for the Flask application factory and built-in routes."""


def test_app_testing_mode(app):  # pylint: disable=redefined-outer-name
    """App is configured with TESTING=True."""
    assert app is not None
    assert app.config["TESTING"] is True


def test_root(client):  # pylint: disable=redefined-outer-name
    """GET / returns 200 with expected response shape."""
    response = client.get("/")
    assert response.status_code == 200
    body = response.get_json()
    assert body["status"] == 200
    assert body["message"] == "Root endpoint"
    assert "app" in body["data"]
    assert "environment" in body["data"]


def test_health(client):  # pylint: disable=redefined-outer-name
    """GET /health returns 200 with healthy=True."""
    response = client.get("/health")
    assert response.status_code == 200
    body = response.get_json()
    assert body["status"] == 200
    assert body["message"] == "Health check OK"
    assert body["data"]["healthy"] is True


def test_status(client):  # pylint: disable=redefined-outer-name
    """GET /status returns 200 with uptime_seconds and environment."""
    response = client.get("/status")
    assert response.status_code == 200
    body = response.get_json()
    assert body["status"] == 200
    assert body["message"] == "Service status"
    assert isinstance(body["data"]["uptime_seconds"], (int, float))
    assert isinstance(body["data"]["environment"], str)
