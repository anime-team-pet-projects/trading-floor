import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()

pytestmark = [
    pytest.mark.django_db,
]


def test_get_detail_user(user_factory) -> None:
    api = APIClient(enforce_csrf_checks=True)

    user = user_factory()

    api.force_authenticate(user)

    response = api.get(reverse('user-detail', kwargs={'pk': user.id}))
    response_content = response.json()

    assert response.status_code == status.HTTP_200_OK, 'Ожидался 200 статус-код ответа'
    assert response_content['id'] == user.id, 'ID из тела ответа не равен ID пользователя, который был запрошен'
    assert (
        response_content['first_name'] == user.first_name
    ), 'Имя из тела ответа не равен имени пользователя, который был запрошен'
    assert response_content.get('email') is None, 'В теле ответа пришёл email, хотя его не ожидалось'


def test_get_detail_unauthorized_user(user_factory) -> None:
    api = APIClient(enforce_csrf_checks=True)

    user = user_factory()

    response = api.get(reverse('user-detail', kwargs={'pk': user.id}))
    response_content = response.json()

    assert response.status_code == status.HTTP_401_UNAUTHORIZED, 'Ожидался 401 статус-код ответа'
    assert (
        response_content['detail'] == 'Authentication credentials were not provided.'
    ), 'Сообщение в поле "detail" не соответствует ожидаемому'
