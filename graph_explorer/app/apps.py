from django.apps import AppConfig
from core.console_main import load_data_source_plagins,load_visualizer_plagins

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    date_source_plagins = []
    visualizer_plagins = []

    def ready(self):
        self.date_source_plagins = load_data_source_plagins()
        self.visualizer_plagins = load_visualizer_plagins()

