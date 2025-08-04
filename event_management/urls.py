from django.urls import path
from django.contrib import admin
from events.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # Event URLs
    path('events/', event_list, name='event_list'),
    path('events/create/', event_create, name='event_create'),
    path('events/<int:event_id>/', event_detail, name='event_detail'),
    path('events/<int:event_id>/update/', event_update, name='event_update'),

    # Participant URLs
    path('participants/', participant_list, name='participant_list'),  # Added list
    path('participants/create/', participant_create, name='participant_create'),
    path('participants/<int:participant_id>/update/', participant_update, name='participant_update'),


    # Category URLs
    path('categories/', category_list, name='category_list'),  # Added list
    path('categories/create/', category_create, name='category_create'),
    path('categories/<int:category_id>/update/', category_update, name='category_update'),

    # Dashboard
    path('dashboard/', organizer_dashboard, name='dashboard'),
]
