import requests
from sofrino_auto_test.utils.attach import logging_response


def api_request(base_api_url, endpoint, method, json=None, params=None):
    url = f"{base_api_url}{endpoint}"
    headers = {
            'content-type': 'application/json; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest'
         }
    response = requests.request(method, url, json=json, params=params, headers=headers)
    logging_response(response)
    return response
