from datetime import datetime, timezone

import pytest

from app import app


@pytest.fixture
def client():
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client


def test_health_returns_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_time_returns_current_utc_iso_timestamp(client):
    before = datetime.now(timezone.utc)
    response = client.get("/time")
    after = datetime.now(timezone.utc)

    assert response.status_code == 200
    stamp = datetime.fromisoformat(response.get_json()["utc_time"])
    assert stamp.tzinfo is not None
    assert stamp.utcoffset().total_seconds() == 0
    assert before <= stamp <= after


def test_unknown_route_returns_404(client):
    assert client.get("/nope").status_code == 404
