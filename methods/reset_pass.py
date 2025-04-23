'''Методы нэймспейса «Password-reset» API web-сервиса «Stellar Burgers».'''
import allure
import requests

from config import API_NEW_PASS, API_RESET_PASS


class ResetPasswordMethods:

    @allure.step('Отправка кода для сброса пароля')
    def code_to_reset_password(self, email):
        return requests.post(url=API_RESET_PASS, data=email)

    @allure.step('Установить новый пароль')
    def set_new_password(self, data):
        return requests.post(url=API_NEW_PASS, data=data)
