import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class APIClient:
    @staticmethod
    def get(endpoint):
        return requests.get(f"{BASE_URL}{endpoint}")

    @staticmethod
    def post(endpoint, payload):
        return requests.post(f"{BASE_URL}{endpoint}", json=payload)

    @staticmethod
    def put(endpoint, payload):
        return requests.put(f"{BASE_URL}{endpoint}", json=payload)

    @staticmethod
    def delete(endpoint):
        return requests.delete(f"{BASE_URL}{endpoint}")