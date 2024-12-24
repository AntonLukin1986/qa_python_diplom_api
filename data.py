'''Статичные данные для API-тестов web-сервиса «Stellar Burgers».'''


# class Common:
#     '''Общие элементы для эндпоинтов.'''
#     ERROR = {'success': False, 'message': None}


class Auth:
    '''Управление пользователями.'''
    ADD = 'A'
    ZERO = 0
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
