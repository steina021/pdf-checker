from django.contrib import admin
from django.urls import path, include

from . import views
from .views import scan_pdf, index

urlpatterns = [
    path('', views.index, name='index'), 
    path('scan-pdf/', scan_pdf, name='scan_pdf'),
    path('api/', include('api.urls')),
]

# Serving media files during development
from django.conf import settings
from django.conf.urls.static import static