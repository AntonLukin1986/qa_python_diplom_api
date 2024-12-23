# Дипломный проект. Задание 2: API-тесты

## API-тестирование сервиса [Stellar Burgers](https://stellarburgers.nomoreparties.site/ "Клик!")

1. Основа: библиотека HTTP-запросов  **requests** и фреймворк **pytest**
2. Дополнительно: фреймворк **Allure** для создания отчётов о результатах тестирования

### Запуск автотестов и создание allure-отчета

1. Установить зависимости: ```pip install -r requirements.txt```
2. Запустить все тесты: ```pytest tests --alluredir=allure_results```
