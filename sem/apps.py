from django.apps import AppConfig


class SemConfig(AppConfig):
    name = 'sem'
    def ready(self):
        import sem.signals

