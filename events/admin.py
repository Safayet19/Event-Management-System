from django.contrib import admin
from .models import Event, Participant, Category

admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(Category)
