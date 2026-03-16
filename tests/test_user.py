from src.assertions.response_validators import ValidateResponse

def test_get_users(api_client):
    response = api_client.get("/users")
    ValidateResponse.status_code(response, 200)
    assert len(response.json()) > 0