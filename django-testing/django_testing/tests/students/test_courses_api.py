import pytest
from django.urls import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.test import APIClient

from students.models import Course


@pytest.mark.django_db
def test_get_course(api_client, course_factory):

    # arrange
    course = course_factory()

    url = reverse("courses-detail", kwargs={'pk': course.id})

    # act
    resp = api_client.get(url)

    # assert
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json
    assert len(resp_json) == 3  # fields count
    assert resp_json['id'] == course.id
    assert resp_json['name'] == course.name


@pytest.mark.django_db
def test_list_courses(api_client, course_factory):

    # arrange
    courses = course_factory(_quantity=10)

    url = reverse("courses-list")

    # act
    resp = api_client.get(url)

    # assert
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json
    assert len(resp_json) == len(courses)
    for i, test_course in enumerate(resp_json):
        assert test_course['id'] == courses[i].id
        assert 'name' in test_course
        assert test_course['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_id_courses(api_client, course_factory):

    # arrange
    course = course_factory()
    course_factory()

    url = reverse("courses-list")

    # act
    resp = api_client.get(url, {'id': course.id})

    # assert
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json
    assert len(resp_json) == 1
    test_course = resp_json[0]
    assert test_course['id'] == course.id


@pytest.mark.django_db
def test_filter_name_courses(api_client, course_factory):

    # arrange
    test_name = 'test1'
    course = course_factory(name=test_name)
    course_factory(name='test2')

    url = reverse("courses-list")

    # act
    resp = api_client.get(url, {'name': test_name})

    # assert
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json
    assert len(resp_json) == 1
    test_course = resp_json[0]
    assert test_course['id'] == course.id
    assert 'name' in test_course
    assert course.name == test_name


@pytest.mark.django_db
def test_create_course(api_client):

    # arrange
    payload = {'name': 'test'}
    url = reverse("courses-list")

    # act
    resp = api_client.post(url, payload)

    # assert

    assert resp.status_code == HTTP_201_CREATED
    resp_json = resp.json()
    assert resp_json
    assert len(resp_json) == 3  # fields count
    assert resp_json['name'] == payload['name']


@pytest.mark.django_db
def test_update_course(api_client, course_factory):

    # arrange
    test_name = 'test_1'
    course = course_factory()
    payload = {'name': test_name}
    url = reverse("courses-detail", kwargs={'pk': course.id})

    # act
    resp = api_client.put(url, payload)

    # assert

    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json
    assert len(resp_json) == 3  # fields count
    assert resp_json['id'] == course.id
    assert resp_json['name'] == payload['name']


@pytest.mark.django_db
def test_delete_course(api_client, course_factory):

    # arrange
    course = course_factory()
    url = reverse("courses-detail", kwargs={'pk': course.id})

    # act
    resp = api_client.delete(url)

    # assert
    assert resp.status_code == HTTP_204_NO_CONTENT

