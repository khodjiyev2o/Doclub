import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.module.models import Course

User = get_user_model()


@pytest.mark.django_db
def test_course_detail(client, new_course):
    url = reverse('course-detail', kwargs={"pk": new_course.id})
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.json().keys()) == [
        'id',
        'title',
        'description',
        'image',
        'speaker',
        'drugs',
        'pharmacist_company',
        'disclaimer',
        'course_files',
        'number_of_modules'
    ]
    assert response.json()['id'] == new_course.id
    assert response.json()['title'] == new_course.title
    assert response.json()['drugs'] == []
    assert response.json()['speaker'] == []
    assert response.json()['disclaimer'] == new_course.disclaimer
    assert response.json()['number_of_modules'] == Course.objects.get(id=new_course.id).modules.count()


@pytest.mark.django_db
def test_course_detail_wrong_pk(client, new_course):
    url = reverse('course-detail', kwargs={"pk": 234543245})
    response = client.get(url)
    assert response.status_code == 404
    assert response.json()['detail'] == 'Not found.'
