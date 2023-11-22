from django.urls import path
from .views import notification_view

urlpatterns = [
    # other URL patterns
    path('notifications/', notification_view, name='notifications'),
]
