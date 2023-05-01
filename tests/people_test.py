from requests import codes
from clients.people.people_client import PeopleClient
from assertpy import assert_that
import pytest

client = PeopleClient()


def test_can_read_one_person():
    response = client.read_person_by_id(1)
    assert_that(response.status_code).is_equal_to(codes.ok)


def test_can_read_all_persons():
    response = client.read_all_persons()
    assert_that(response.status_code).is_equal_to(codes.ok)
