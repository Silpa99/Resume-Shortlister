from django.apps import AppConfig


class WebAppConfig(AppConfig):
    name = 'web_app'
    def ready(self):
    	import web_app.signals