from clients.people.base_client import BaseClient
from utils.request import APIRequest
from config import BASE_URI

from uuid import uuid4
from json import dumps


class PeopleClient(BaseClient):
    def __init__(self):
        self.base_url = BASE_URI
        self.request = APIRequest()

    def create_person(self, body=None):
        last_name, response = self.__create_person_with_unique_last_name(body)
        return last_name, response

    def read_all_persons(self):
        return self.request.get(self.base_url)

    def read_person_by_id(self, person_id):
        url = f'{BASE_URI}/{person_id}'
        return self.request.get(url)

    def update_person_by_id(self, person_id, body):
        url = f'{BASE_URI}/{person_id}'
        payload = dumps(body)
        return self.request.put(url, payload, self.headers)

    def delete_person_by_id(self, person_id):
        url = f'{BASE_URI}/{person_id}'
        return self.request.delete(url)

    def __create_person_with_unique_last_name(self, body=None):
        if body is None:
            last_name = f'Last_name {str(uuid4())}'
            payload = dumps({
                'fname': 'First_name',
                'lname': last_name
            })
        else:
            last_name = body['lname']
            payload = dumps(body)

        response = self.request.post(self.base_url, payload, self.headers)

        return last_name, response
