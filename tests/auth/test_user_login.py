'''Тесты эндпоинта для авторизации пользователей.'''
import allure
import pytest

from data import ZERO


class TestUserLogin:

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
        user_data[field] = ZERO
        status_code, body = auth_methods.login_user(user_data, token)
        assert status_code == 401  # and проверка тела
