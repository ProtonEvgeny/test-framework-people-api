from dataclasses import dataclass
import requests
from requests.exceptions import JSONDecodeError


@dataclass
class Response:
    status_code: int
    body: str
    json_body: object
    headers: dict


class APIRequest:
    def get(self, url):
        response = requests.get(url)
        return self.__get_response(response)

    def post(self, url, payload, headers):
        response = requests.post(url=url, data=payload, headers=headers)
        return self.__get_response(response)

    def delete(self, url):
        response = requests.delete(url)
        return self.__get_response(response)

    def put(self, url, payload, headers):
        response = requests.put(url=url, data=payload, headers=headers)
        return self.__get_response(response)

    def __get_response(self, response):
        status_code = response.status_code
        body = response.text

        try:
            json_body = response.json()
        except JSONDecodeError:
            json_body = {}

        headers = response.headers

        return Response(status_code, body, json_body, headers)
