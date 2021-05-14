import pytest
from django.urls import reverse
from rest_framework.status import HTTP_201_CREATED
from rest_framework.test import APIClient

from students.models import Course


@pytest.mark.django_db
def test_create_course():
    url = reverse("courses-list")
    client = APIClient()
    resp = client.get(url)
    # assert resp.status_code == HTTP_201_CREATED
    resp_json = resp.json()
    # c = Course.objects.create(name='test')
    # assert c.id
    # assert c.name == 'test'
