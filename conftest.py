'''Фикстуры для API-тестов web-сервиса «Stellar Burgers».'''
import pytest

from helpers import get_user_data
from methods.auth import AuthMethods
from methods.orders import OrdersMethods


@pytest.fixture(scope='session')
def auth_methods():
    return AuthMethods()


@pytest.fixture(scope='session')
def orders_methods():
    return OrdersMethods()


@pytest.fixture(scope='function')
def test_user(auth_methods):
    '''Регистрация тестового пользователя с последующим удалением.'''
    user_data = get_user_data()
    token = auth_methods.register_user(user_data).json().get('accessToken')
    yield user_data, token
    auth_methods.delete_user(token)


@pytest.fixture(scope='function')
def existing_email(auth_methods):
    '''Регистрация тестового пользователя с последующим удалением.
    Для теста с изменением email пользователя на уже существующий.'''
    body = auth_methods.register_user(get_user_data()).json()
    yield body['user']['email']
    auth_methods.delete_user(body.get('accessToken'))
