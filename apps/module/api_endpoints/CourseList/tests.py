import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.module.models import Course
User = get_user_model()


@pytest.mark.django_db
def test_course_list(client, new_course):
    url = reverse('course-list')
    response = client.get(url)
    assert response.status_code == 200
    assert response.json()['count'] == Course.objects.count()
    assert list(response.json()['results'][0].keys()) == [
        'id',
        'title',
        'description',
        'image',
        'speaker',
    ]


@pytest.mark.django_db
def test_course_list_not_found(client):
    url = reverse('course-list')
    response = client.get(url)
    assert response.status_code == 200
    assert response.json()['count'] == 0
    assert response.json()['results'] == []