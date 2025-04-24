from django.contrib import admin
from django.urls import path, include

from . import views
from .views import index

urlpatterns = [
    path('', views.index, name='index'), 
    path('api/', include('api.urls')),
]

# Serving media files during development
from django.conf import settings
from django.conf.urls.static import static