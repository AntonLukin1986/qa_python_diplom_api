'''Статичные данные для API-тестов web-сервиса «Stellar Burgers».'''
ADD = 'A'
ZERO = 0


class Auth:
    '''Управление пользователями.'''
    NO_EMAIL = {'name': 'test', 'password': 'test'}
    NO_NAME = {'email': 'test', 'password': 'test'}
    NO_PASSWORD = {'email': 'test', 'name': 'test'}


    # сдвигать вверх по мере применение, чтобы лишних не оказалось
    CREATED = 200, ('success', 'user', 'accessToken', 'refreshToken')
    LOGGED_IN = 200, ('success', 'user', 'accessToken', 'refreshToken')
    CHANGED = 200, ('success', 'user')

    WRONG_FIELD = 401, {'success': False, 'message': 'email or password are incorrect'}
    UNAUTHORIZED = 401, {'success': False, 'message': 'You should be authorised'}
    DUPLICATE = 403, {'success': False, 'message': 'User already exists'}
    EMAIL_EXISTS = 403, {'success': False, 'message': 'User with such email already exists'}
    MISSED_FIELD = 403, {'success': False, 'message': 'Email, password and name are required fields'}


class Orders:
    '''Управление заказами.'''
    CREATED_NO_AUTH = 200, {"success": True, "name": "...", "order": {"number": int}}
    CREATED_AUTH = 200, ...
    ORDERS_OK = 200, ...
    NO_IDS = 400, ...
    WRONG_IDS = 500, ...
    UNAUTHORIZED = 401, {'success': False, 'message': 'You should be authorised'}
