import pytest
from src.api_client import APIClient

@pytest.mark.smoke
def test_get_posts():
    resp = APIClient.get("/posts")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    assert len(resp.json()) > 0

# def test_get_post_by_id():
#     resp = APIClient.get("/posts/1")
#     assert resp.status_code == 200
#     data = resp.json()
#     assert data["id"] == 1
#     assert "title" in data

# def test_create_post():
#     payload = {"title": "Test Post", "body": "Content", "userId": 1}
#     resp = APIClient.post("/posts", payload)
#     assert resp.status_code == 201
#     assert resp.json()["title"] == "Test Post"

# def test_delete_post():
#     resp = APIClient.delete("/posts/1")
#     assert resp.status_code == 200  # JSONPlaceholder returns 200