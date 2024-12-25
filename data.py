'''Статичные данные для API-тестов web-сервиса «Stellar Burgers».'''
ADD = 'A'
UNAUTHORIZED = 401, 'You should be authorised'
ZERO = 0


class Auth:
    '''Управление пользователями.'''
    NO_EMAIL = {'name': 'test', 'password': 'test'}
    NO_NAME = {'email': 'test', 'password': 'test'}
    NO_PASSWORD = {'email': 'test', 'name': 'test'}


    # сдвигать вверх по мере применение, чтобы лишних не оказалось
    CHANGED = 200, ('user',)
    CREATED = 200, ('user', 'accessToken', 'refreshToken')
    LOGGED_IN = 200, ('user', 'accessToken', 'refreshToken')

    DUPLICATE = 403, 'User already exists'
    EMAIL_EXISTS = 403, 'User with such email already exists'
    MISSED_FIELD = 403, 'Email, password and name are required fields'
    WRONG_FIELD = 401, 'email or password are incorrect'


class Orders:
    '''Управление заказами.'''


    # сдвигать вверх по мере применение, чтобы лишних не оказалось
    CREATED_AUTH = 200, ...
    CREATED_NO_AUTH = 200, {"name": "...", "order": {"number": int}}
    ORDERS_OK = 200, ...

    NO_IDS = 400, 'Ingredient ids must be provided'
    WRONG_IDS = 500, 'Internal Server Error'
