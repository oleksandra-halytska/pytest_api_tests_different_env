import requests
# piu

class TestPytestMultiEnv:
    def test_get_multi_env(
            self, env_config, env_request_data, env_response_data
    ):
        host = env_config["host"]
        get_api = env_config["getAPI"]
        get_api_response_data = env_response_data["getAPI"]
        response = requests.get(host + get_api)

        assert response.status_code == 200
        assert response.json() == get_api_response_data

    def test_post_multi_env(
            self, env_config, env_request_data, env_response_data
    ):
        host = env_config["host"]
        post_api = env_config["postAPI"]
        post_api_request_data = env_request_data["postAPI"]
        post_api_response_data = env_response_data["postAPI"]
        response = requests.post(host + post_api, post_api_request_data)

        assert response.status_code == 201
        assert response.json() == post_api_response_data
