import requests
import json
from sofrino_auto_test.utils.attach import logging_response, response_logging, response_attaching


def api_request(base_api_url, endpoint, method, params=None):
    url = f"{base_api_url}{endpoint}"
    data = json.dumps(params)
    headers = {
            'content-type': 'application/json; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest'
         }
    response = requests.request(method, url, headers=headers, params=params, data=data, json=json)
    response_logging(response)
    response_attaching(response)
    return response
