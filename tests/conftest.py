"""Pytest fixtures for the Flask application test suite."""

import pytest

from app import create_app


@pytest.fixture()
def app():
    """Create and configure a Flask app instance for tests."""
    flask_app = create_app()
    flask_app.config.update(
        {
            "TESTING": True,
            "ENVIRONMENT": "testing",
            "DEBUG": False,
        }
    )
    yield flask_app


@pytest.fixture()
def client(app):  # pylint: disable=redefined-outer-name
    """Return a Flask test client for the configured app fixture."""
    return app.test_client()
