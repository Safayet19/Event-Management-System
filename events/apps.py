from django.apps import AppConfig
from django.core.management import call_command
import os
from django.db.utils import OperationalError

class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events'

    def ready(self):
        if os.environ.get('LOAD_FIXTURE_ON_STARTUP') == 'true':
            try:
                call_command('loaddata', 'data.json')
            except OperationalError:
                pass  # Database not ready yet
