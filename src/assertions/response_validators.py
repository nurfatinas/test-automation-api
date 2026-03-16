class ValidateResponse:

    @staticmethod
    def status_code(response, expected):
        assert response.status_code == expected

    @staticmethod
    def key_exists(response, key):
        assert key in response.json()

    @staticmethod
    def value_equals(actual, expected):
        assert actual == expected