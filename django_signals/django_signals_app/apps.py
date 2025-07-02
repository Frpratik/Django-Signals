from django.apps import AppConfig


class DjangoSignalsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_signals_app'

    def ready(self):
        import django_signals_app.signals