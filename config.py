'''Данные API web-сервиса «Stellar Burgers».'''
API_BASE = 'https://stellarburgers.nomoreparties.site/api/'

API_AUTH = API_BASE + 'auth/'
API_AUTH_LOGIN = API_AUTH + 'login'
API_AUTH_REGISTER = API_AUTH + 'register'
API_AUTH_USER = API_AUTH + 'user'

API_RESET_PASS = API_BASE + 'password-reset'
API_NEW_PASS = API_RESET_PASS + '/reset'

API_INGREDIENTS = API_BASE + 'ingredients'
API_ORDERS = API_BASE + 'orders'
API_ALL_ORDERS = API_ORDERS + '/all'
