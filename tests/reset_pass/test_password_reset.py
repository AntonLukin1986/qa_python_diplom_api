'''Тесты эндпоинта для восстановления пароля.'''
import allure

from data import ResetPassword
from helpers import code_and_body_are_expected


class TestResetPassword:

    @allure.title('Успешная отправка кода для сброс пароля')
    def test_code_to_reset_password_success(
        self, reset_pass_methods, test_user
    ):
        user_data, _ = test_user
        response = reset_pass_methods.code_to_reset_password(user_data['email'])
        expected_code, expected_body = ResetPassword.CODE
        assert (response.status_code == expected_code and
                response.json() == expected_body)

    @allure.title('Ошибка при неверном токене смены пароля')
    def test_wrong_token_reset_password_failed(self, reset_pass_methods):
        response = reset_pass_methods.set_new_password(
            ResetPassword.NEW_PASS_DATA
        )
        result, message = code_and_body_are_expected(
            response, *ResetPassword.BAD_TOKEN
        )
        assert result, message
