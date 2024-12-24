'''Тесты эндпоинта для управления пользователями.'''
import allure
import pytest

from data import Auth
from helpers import get_user_data


class TestAuth:

    @allure.title('Успешная регистрация нового пользователя')
    def test_register_user_success(self, auth_methods):
        status_code, body = auth_methods.register_user(get_user_data())
        auth_methods.delete_user(body.get('accessToken'))
        assert status_code == 200  # and проверка тела

    @allure.title('Невозможно создать двух одинаковых пользователей')
    def test_register_user_duplicate_error(self, auth_methods, test_user):
        user_data, _ = test_user
        status_code, body = auth_methods.register_user(user_data)
        assert status_code == 403  # and проверка тела

    @allure.title('Невозможно создать пользователя без email / пароля / имени')
    @pytest.mark.parametrize(
        'data', [pytest.param(Auth.NO_NAME, id='no name'),
                 pytest.param(Auth.NO_PASSWORD, id='no pass'),
                 pytest.param(Auth.NO_EMAIL, id='no email')]
    )
    def test_register_user_missed_field_error(self, auth_methods, data):
        status_code, body = auth_methods.register_user(data)
        assert status_code == 403  # and проверка тела

    @allure.title('Успешная авторизация пользователя')
    def test_login_user_success(self, auth_methods, test_user):
        status_code, body = auth_methods.login_user(*test_user)
        assert status_code == 200, f'{body}'

    @allure.title('Ошибка авторизации с неверным email или паролем')
    @pytest.mark.parametrize(
        'field', [pytest.param('password', id='wrong pass'),
                  pytest.param('email', id='wrong email')]
    )
    def test_login_user_wrong_field_error(self, auth_methods, test_user, field):
        user_data, token = test_user
        user_data[field] = Auth.ZERO
        status_code, body = auth_methods.login_user(user_data, token)
        assert status_code == 401  # and проверка тела

    @allure.title('Успешное изменение данных пользователя')
    @pytest.mark.parametrize(
        'field', [pytest.param('password', id='password'),
                  pytest.param('email', id='email'),
                  pytest.param('name', id='name')]
    )
    def test_change_user_data_success(self, auth_methods, test_user, field):
        user_data, token = test_user
        to_change = {field: user_data[field] + Auth.ADD}
        status_code, body = auth_methods.change_user(to_change, token)
        assert status_code == 200  # and проверка тела

    @allure.title('Невозможно изменить данные пользователя без авторизации')
    def test_change_user_data_no_token_error(self, auth_methods):
        to_change = {'email': 'test', 'password': 'test', 'name': 'test'}
        status_code, body = auth_methods.change_user(to_change, None)
        assert status_code == 401  # and проверка тела

    @allure.title('Невозможно сменить email пользователя на уже существующий')
    def test_change_user_email_exists_error(self, auth_methods, test_user, existing_email):
        _, token = test_user
        to_change = {'email': existing_email}
        status_code, body = auth_methods.change_user(to_change, token)
        assert status_code == 403  # and проверка тела
