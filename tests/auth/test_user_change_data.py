'''Тесты эндпоинта для изменения данных пользователя.'''
import allure
import pytest

from data import Auth, Common
from helpers import code_and_body_are_expected


class TestUserChangeData:

    @allure.title('Успешное изменение данных пользователя')
    @pytest.mark.parametrize(
        'field', [pytest.param('password', id='password'),
                  pytest.param('email', id='email'),
                  pytest.param('name', id='name')]
    )
    def test_change_user_data_success(self, auth_methods, test_user, field):
        user_data, token = test_user
        to_change = {field: user_data[field] + Common.ADD}
        response = auth_methods.change_user_data(to_change, token)
        result, message = code_and_body_are_expected(response, *Auth.CHANGED)
        assert result, message

    @allure.title('Невозможно изменить данные пользователя без авторизации')
    def test_change_user_data_no_token_error(self, auth_methods):
        to_change = {'email': 'test', 'password': 'test', 'name': 'test'}
        response = auth_methods.change_user_data(to_change)
        result, message = code_and_body_are_expected(
            response, *Common.UNAUTHORIZED
        )
        assert result, message

    @allure.title('Невозможно сменить email пользователя на уже существующий')
    def test_change_user_email_exists_error(
        self, auth_methods, test_user, existing_email
    ):
        _, token = test_user
        to_change = {'email': existing_email}
        response = auth_methods.change_user_data(to_change, token)
        result, message = code_and_body_are_expected(
            response, *Auth.EMAIL_EXISTS
        )
        assert result, message
