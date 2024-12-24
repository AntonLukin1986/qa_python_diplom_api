'''Тесты эндпоинта для регистрации пользователей.'''
import allure
import pytest

from data import Auth
from helpers import get_user_data


class TestUserRegister:

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
