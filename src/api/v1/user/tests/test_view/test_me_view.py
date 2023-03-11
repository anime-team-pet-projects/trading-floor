import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()

pytestmark = [
    pytest.mark.django_db,
]


def test_get_me(user_data: dict) -> None:
    api = APIClient(enforce_csrf_checks=True)

    user = User(**user_data)
    user.save()

    api.force_authenticate(user)

    response = api.get(reverse('user-me'))
    response_content = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_content['id'] == user.id
    assert response_content['first_name'] == user.first_name
    assert response_content['email'] == user.email


def test_get_me_without_jwt(user_data: dict) -> None:
    api = APIClient(enforce_csrf_checks=True)

    response = api.get(reverse('user-me'))
    response_content = response.json()

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response_content['detail'] == 'Authentication credentials were not provided.'


def test_update_me(user_data: dict) -> None:
    api = APIClient(enforce_csrf_checks=True)

    user = User(**user_data)
    user.save()

    api.force_authenticate(user)

    assert user.first_name == user_data['first_name']

    user_data['first_name'] = 'ChangeFirstName'
    user_data['last_name'] = 'ChangeLastName'

    response = api.patch(reverse('user-me'), user_data)
    response_content = response.json()

    user.refresh_from_db()

    assert response.status_code == status.HTTP_200_OK
    assert response_content['first_name'] == user.first_name


def test_invalid_update_me(user_data: dict) -> None:
    api = APIClient(enforce_csrf_checks=True)

    user = User(**user_data)
    user.save()

    api.force_authenticate(user)

    old_email = user.email
    assert user.email == user_data['email']

    user_data['email'] = 'test@gmail.com'
    response = api.patch(reverse('user-me'), user_data)

    user.refresh_from_db()

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert user.email == old_email


def test_delete_me(user_data: dict) -> None:
    api = APIClient(enforce_csrf_checks=True)

    user = User(**user_data)
    user.save()

    api.force_authenticate(user)

    assert user.email == user_data['email']
    assert user.is_active

    response = api.delete(reverse('user-me'))

    user.refresh_from_db()

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not user.is_active
