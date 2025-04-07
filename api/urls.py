from django import urls
from django.urls import path
from .views import get_logs, create_log

urlpatterns = [
    path('loggers/', get_logs, name='get_logs'),
    path('loggers/create', create_log, name='create_log'),
]