from django.apps import AppConfig

from core.src.core.core import Core


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    core: Core

    def ready(self):
        self.core = Core()

