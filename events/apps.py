from django.apps import AppConfig
from django.core.management import call_command
import os

class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events'

    def ready(self):
        print("EventsConfig.ready() called") 
        if os.environ.get('LOAD_FIXTURE_ON_STARTUP') == 'true':
            try:
                call_command('loaddata', 'data.json')
                print("Data loaded successfully!")
            except Exception as e:
                print(f"Error loading data: {e}")
