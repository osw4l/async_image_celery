from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'uploader.apps.app'

    def ready(self):
    	from . import signals