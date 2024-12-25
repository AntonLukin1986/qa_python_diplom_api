'''Тесты эндпоинта для регистрации пользователей.'''
import allure
import pytest

from data import Auth
from helpers import code_and_body_are_expected, get_user_data


class TestUserRegister:

    @allure.title('Успешная регистрация нового пользователя')
    def test_register_user_success(self, auth_methods):
        response = auth_methods.register_user(get_user_data())
        auth_methods.delete_user(response.json().get('accessToken'))
        result, message = code_and_body_are_expected(response, *Auth.CREATED)
        assert result, message

    @allure.title('Невозможно создать двух одинаковых пользователей')
    def test_register_user_duplicate_error(self, auth_methods, test_user):
        user_data, _ = test_user
        response = auth_methods.register_user(user_data)
        result, message = code_and_body_are_expected(response, *Auth.DUPLICATE)
        assert result, message

    @allure.title('Невозможно создать пользователя без email / пароля / имени')
    @pytest.mark.parametrize(
        'data', [pytest.param(Auth.NO_NAME, id='no name'),
                 pytest.param(Auth.NO_PASSWORD, id='no pass'),
                 pytest.param(Auth.NO_EMAIL, id='no email')]
    )
    def test_register_user_missed_field_error(self, auth_methods, data):
        response = auth_methods.register_user(data)
        result, message = code_and_body_are_expected(
            response, *Auth.MISSED_FIELD
        )
        assert result, message
