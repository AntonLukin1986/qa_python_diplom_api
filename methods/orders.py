'''Методы нэймспейса «Orders» API web-сервиса «Stellar Burgers».'''
import random

import allure
import requests

from config import API_INGREDIENTS, API_ORDERS


class OrdersMethods:

    @allure.step('Получение списка ингредиентов')
    def get_ingredients(self):
        response = requests.get(url=API_INGREDIENTS)
        return response.status_code, response.json()

    @allure.step('Создание нового заказа')
    def make_order(self, ingredients_ids, token):
        response = requests.post(
            url=API_ORDERS,
            data={'ingredients': ingredients_ids},
            headers={'Authorization': token}
        )
        return response.status_code, response.json() if response.ok else response

    @allure.step('Получение заказов пользователя')
    def get_user_orders(self, token):
        response = requests.get(
            url=API_ORDERS, headers={'Authorization': token}
        )
        return response.status_code, response.json()
