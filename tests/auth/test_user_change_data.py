'''Тесты эндпоинта для изменения данных пользователя.'''
import allure
import pytest

from data import ADD


class TestUserChangeData:

    @allure.title('Успешное изменение данных пользователя')
    @pytest.mark.parametrize(
        'field', [pytest.param('password', id='password'),
                  pytest.param('email', id='email'),
                  pytest.param('name', id='name')]
    )
    def test_change_user_data_success(self, auth_methods, test_user, field):
        user_data, token = test_user
        to_change = {field: user_data[field] + ADD}
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
