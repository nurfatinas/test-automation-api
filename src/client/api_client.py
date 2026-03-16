import requests
import json

class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def _log_request(self, method, url, headers=None, payload=None):

        print("\n========== API REQUEST ==========")
        print(f"METHOD : {method}")
        print(f"URL    : {url}")

        if headers:
            print("HEADERS:")
            print(json.dumps(headers, indent=2))

        if payload:
            print("BODY:")
            print(json.dumps(payload, indent=2))

    def _log_response(self, response):

        print("\n========== API RESPONSE ==========")
        print(f"STATUS : {response.status_code}")

        try:
            print("BODY:")
            print(json.dumps(response.json(), indent=2))
        except Exception:
            print(response.text)

        print("==================================\n")

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"

        self._log_request("GET", url, headers, params)
        response = requests.get(url, params=params, headers=headers)
        self._log_response(response)

        return response


    def post(self, endpoint, json=None, headers=None):
        url = f"{self.base_url}{endpoint}"

        self._log_request("POST", url, headers, json)
        response = requests.post(url, json=json, headers=headers)
        self._log_response(response)

        return response


    def put(self, endpoint, json=None, headers=None):
        url = f"{self.base_url}{endpoint}"

        self._log_request("PUT", url, headers, json)
        response = requests.put(url, json=json, headers=headers)
        self._log_response(response)

        return response


    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"

        self._log_request("DELETE", url, headers)
        response = requests.delete(url, headers=headers)
        self._log_response(response)

        return response