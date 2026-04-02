from __future__ import annotations


def test_create_note_returns_201(client):
    response = client.post(
        "/notes/create",
        json={"title": "Test Note", "content": "Hello DB!", "tags": ["test"]},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Note"
    assert data["content"] == "Hello DB!"
    assert data["tags"] == ["test"]
    assert "id" in data
    assert "created_at" in data


def test_create_note_invalid_returns_422(client):
    response = client.post("/notes/create", json={})
    assert response.status_code == 422


def test_get_note_returns_200(client):
    create_resp = client.post(
        "/notes/create",
        json={"title": "Get Me", "content": "Find this note"},
    )
    note_id = create_resp.json()["id"]

    response = client.get(f"/notes/{note_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Get Me"


def test_get_note_not_found_returns_404(client):
    response = client.get("/notes/nonexistent-id")
    assert response.status_code == 404


def test_search_notes_returns_200(client):
    client.post(
        "/notes/create",
        json={"title": "Searchable", "content": "Find me by search"},
    )

    response = client.post(
        "/notes/search",
        json={"query": "Searchable", "limit": 10},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["total"] >= 1
    assert data["results"][0]["title"] == "Searchable"


def test_delete_note_returns_204(client):
    create_resp = client.post(
        "/notes/create",
        json={"title": "Delete Me", "content": "Goodbye"},
    )
    note_id = create_resp.json()["id"]

    response = client.delete(f"/notes/{note_id}")
    assert response.status_code == 204

    get_resp = client.get(f"/notes/{note_id}")
    assert get_resp.status_code == 404


def test_delete_note_not_found_returns_404(client):
    response = client.delete("/notes/nonexistent-id")
    assert response.status_code == 404
