from django import urls
from django.urls import path
from .views import create_log

urlpatterns = [
    path('loggers/create', create_log, name='create_log'),
]