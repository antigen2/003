___---=== settings.py===---___

Прописываем переменные:
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

приложение account прописываем первым в INSTALLED_APPS = [...]
--------------------------------

buglist:

1. При повторной авторизации авторизированного пользователя
вылетает в ошибку.
