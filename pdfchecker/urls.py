from django.urls import path
from . import views
from .views import scan_pdf, index

urlpatterns = [
    path('', views.index, name='index'), 
    path('scan-pdf/', scan_pdf, name='scan_pdf'),
]

# Serving media files during development
from django.conf import settings
from django.conf.urls.static import static