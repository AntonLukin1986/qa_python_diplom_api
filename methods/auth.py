'''Методы нэймспейса «Auth» API web-сервиса «Stellar Burgers».'''
import allure
import requests

from config import API_AUTH_LOGIN, API_AUTH_REGISTER, API_AUTH_USER


class AuthMethods:

    @allure.step('Регистрация нового пользователя')
    def register_user(self, user_data):
        return requests.post(url=API_AUTH_REGISTER, data=user_data)

    @allure.step('Удаление аккаунта пользователя')
    def delete_user(self, token):
        return requests.delete(
            url=API_AUTH_USER, headers={'Authorization': token}
        )

    @allure.step('Авторизация пользователя')
    def login_user(self, user_data, token):
        return requests.post(
            url=API_AUTH_LOGIN,
            data=user_data,
            headers={'Authorization': token}
        )

    @allure.step('Изменение данных пользователя')
    def change_user_data(self, to_change, token=None):
        return requests.patch(
            url=API_AUTH_USER, data=to_change, headers={'Authorization': token}
        )
