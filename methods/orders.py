'''Методы нэймспейса «Orders» API web-сервиса «Stellar Burgers».'''
import allure
import requests

from config import API_ALL_ORDERS, API_INGREDIENTS, API_ORDERS


class OrdersMethods:

    @allure.step('Получение списка ингредиентов')
    def get_ingredients(self):
        return requests.get(url=API_INGREDIENTS)

    @allure.step('Создание нового заказа')
    def make_order(self, ingredients_ids, token):
        return requests.post(
            url=API_ORDERS,
            data={'ingredients': ingredients_ids},
            headers={'Authorization': token}
        )

    @allure.step('Получение заказов пользователя')
    def get_user_orders(self, token):
        return requests.get(
            url=API_ORDERS, headers={'Authorization': token}
        )

    @allure.step('Получение всех заказов')
    def get_all_orders(self):
        return requests.get(url=API_ALL_ORDERS)
