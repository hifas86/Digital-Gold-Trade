from django.apps import AppConfig

class GoldtradeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'goldtrade'

    def ready(self):
        import goldtrade.signals
