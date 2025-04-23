'''Тесты эндпоинта для получения ингредиентов.'''
import json
import allure


class TestGetIngredients:

    @allure.title('Получение списка ингредиентов')
    def test_get_ingredients_success(self, orders_methods):
        response = orders_methods.get_ingredients()
        with open('response_ingredients.json', encoding='utf-8') as f:
            expected_body = json.load(f)
        assert response.status_code == 200 and response.json() == expected_body
