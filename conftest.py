import pytest
from src.client.api_client import APIClient
from src.utils.read_config import ReadConfig

@pytest.fixture(scope="session")
def api_client():

    config = ReadConfig.load_config()

    return APIClient(config["base_url"])