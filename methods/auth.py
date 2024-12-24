'''Методы нэймспейса «Auth» API web-сервиса «Stellar Burgers».'''
import allure
import requests

from config import API_AUTH_LOGIN, API_AUTH_REGISTER, API_AUTH_USER


class AuthMethods:

    @allure.step('Регистрация нового пользователя')
    def register_user(self, user_data):
        response = requests.post(url=API_AUTH_REGISTER, data=user_data)
        return response.status_code, response.json()

    @allure.step('Удаление аккаунта пользователя')
    def delete_user(self, token):
        response = requests.delete(
            url=API_AUTH_USER, headers={'Authorization': token}
        )
        return response.status_code, response.json()

    @allure.step('Авторизация пользователя')
    def login_user(self, user_data, token):
        response = requests.post(
            url=API_AUTH_LOGIN,
            data=user_data,
            headers={'Authorization': token}
        )
        return response.status_code, response.json()

    @allure.step('Изменение данных пользователя')
    def change_user(self, to_change, token):
        response = requests.patch(
            url=API_AUTH_USER, data=to_change, headers={'Authorization': token}
        )
        return response.status_code, response.json()
