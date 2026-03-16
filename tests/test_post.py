from src.assertions.response_validators import ValidateResponse
from src.data.test_data import create_post_payload


def test_get_post(api_client):

    response = api_client.get("/posts/1")

    ValidateResponse.status_code(response, 200)
    ValidateResponse.value_equals(response.json()["id"], 1)


def test_create_post(api_client):

    response = api_client.post("/posts", json=create_post_payload)

    ValidateResponse.status_code(response, 201)