import pytest
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from tests.factories import CertificateFactory


@pytest.mark.django_db
def test_generate_certificate_existing(client, new_user):
    new_certificate = CertificateFactory(user=new_user)

    url = reverse('generate-certificate')
    data = {"course": new_certificate.course.id, "full_name": "SAMANDAR"}
    jwt = RefreshToken.for_user(new_user).access_token
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {jwt}"
    }
    response = client.post(url, data=data, **headers)

    assert response.status_code == 200
    assert response.data['course'] == new_certificate.course.id
    assert response.data['course'] == new_certificate.course.id
    assert response.data['user'] == new_certificate.user.id
    assert response.data['cid'] == new_certificate.cid


@pytest.mark.django_db
def test_generate_certificate_eligible(client, new_user, new_certificate):
    url = reverse('generate-certificate')
    data = {"course": new_certificate.course.id, "full_name": "SAMANDAR"}
    jwt = RefreshToken.for_user(new_user).access_token
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {jwt}"
    }
    response = client.post(url, data=data, **headers)
    assert response.status_code == 201
    assert response.data['course'] == new_certificate.course.id
    assert response.data['course'] == new_certificate.course.id
    assert response.data['user'] == new_user.id
    assert response.data['cid'] != new_certificate.cid

@pytest.mark.django_db
def test_generate_certificate_unauthenticated(client, new_course):
    url = reverse('generate-certificate')
    data = {"course": new_course.id}
    response = client.post(url, data)
    assert response.status_code == 401



