from django.apps import AppConfig
from django.apps import AppConfig


class LoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login'


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import login.signals
