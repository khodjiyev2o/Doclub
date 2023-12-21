import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_module_detail(client, new_module):
    url = reverse('module-detail', kwargs={"pk": new_module.id})
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.json().keys()) == [
        'id',
        'title',
        'cover_image',
        'tags',
        'speaker',
        'drugs',
        'pharmacist_company',
        'module_files',
        'disclaimer',
    ]
    assert response.json()['id'] == new_module.id
    assert response.json()['title'] == new_module.title
    assert response.json()['tags'] == []
    assert response.json()['speaker'] == []
    assert response.json()['disclaimer'] == new_module.disclaimer


@pytest.mark.django_db
def test_module_detail_wrong_pk(client, new_module):
    url = reverse('module-detail', kwargs={"pk": 234543245})
    response = client.get(url)
    assert response.status_code == 404
    assert response.json()['detail'] == 'Not found.'
