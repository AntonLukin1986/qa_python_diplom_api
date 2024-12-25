'''Тесты эндпоинта для авторизации пользователей.'''
import allure
import pytest

from data import Auth, Common
from helpers import code_and_body_are_expected


class TestUserLogin:

    @allure.title('Успешная авторизация пользователя')
    def test_login_user_success(self, auth_methods, test_user):
        response = auth_methods.login_user(*test_user)
        result, message = code_and_body_are_expected(response, *Auth.LOGGED_IN)
        assert result, message

    @allure.title('Ошибка авторизации с неверным email или паролем')
    @pytest.mark.parametrize(
        'field', [pytest.param('password', id='wrong pass'),
                  pytest.param('email', id='wrong email')]
    )
    def test_login_user_wrong_field_error(
        self, auth_methods, test_user, field
    ):
        user_data, token = test_user
        user_data[field] = Common.ZERO
        response = auth_methods.login_user(user_data, token)
        result, message = code_and_body_are_expected(
            response, *Auth.WRONG_FIELD
        )
        assert result, message
