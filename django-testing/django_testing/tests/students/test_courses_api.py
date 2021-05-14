import pytest
from django.urls import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.test import APIClient

from students.models import Course


@pytest.mark.django_db
def test_list_courses():

    # arrange
    course = Course.objects.create(name='test')

    url = reverse("courses-list")
    client = APIClient()

    # act
    resp = client.get(url)

    # assert

    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json
    assert len(resp_json) == 1
    test_course = resp_json[0]
    assert test_course['id'] == course.id
    assert 'name' in test_course
    assert course.name == 'test'
