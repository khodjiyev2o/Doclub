import pytest
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from tests.factories import UserModuleCompletionRequirementsFactory


@pytest.mark.django_db
def test_user_module_requirements_detail(client, new_user, new_module):
    user_module_completion_requirements = UserModuleCompletionRequirementsFactory(user=new_user, module=new_module)
    url = reverse('user-module-requirements', kwargs={"pk": user_module_completion_requirements.module.id})
    jwt = RefreshToken.for_user(new_user).access_token
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {jwt}"
    }
    response = client.get(url, **headers)
    assert response.status_code == 200
    assert list(response.json().keys()) == [
        'is_video_played',
        'is_files_downloaded',
        'is_test_passed',
        'can_certificate_be_issued',
    ]
    assert response.data['is_files_downloaded'] == user_module_completion_requirements.is_files_downloaded
    assert response.data['is_video_played'] == user_module_completion_requirements.is_video_played
    assert response.data['is_test_passed'] == user_module_completion_requirements.is_test_passed


@pytest.mark.django_db
def test_user_module_requirements_detail_unauthenticated(client, new_user, user_module_completion_requirements):
    url = reverse('user-module-requirements', kwargs={"pk": user_module_completion_requirements.module.id})
    response = client.get(url)
    assert response.status_code == 401
