import httpx
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_note_returns_201():
    response = client.post(
        "/notes/create",
        json={"title": "Test Note", "content": "Hello world", "tags": ["demo"]},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Note"
    assert data["content"] == "Hello world"
    assert "id" in data
    assert "created_at" in data


def test_create_note_invalid_returns_422():
    response = client.post("/notes/create", json={})
    assert response.status_code == 422


def test_search_notes_returns_200():
    response = client.post("/notes/search", json={"query": "test"})
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert "total" in data
    assert data["results"] == []
    assert data["total"] == 0


def test_external_call_with_monkeypatch(monkeypatch):
    """Example: mock httpx.get so we don't hit the real network."""

    class FakeResponse:
        status_code = 200

        def json(self):
            return {"title": "Mocked post", "id": 1}

    monkeypatch.setattr(httpx, "get", lambda *args, **kwargs: FakeResponse())

    result = httpx.get("https://jsonplaceholder.typicode.com/posts/1")
    assert result.status_code == 200
    assert result.json()["title"] == "Mocked post"
