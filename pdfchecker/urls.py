from django.urls import path
from . import views
from .views import scan_pdf, index 

urlpatterns = [
    path('', views.index),
    path('scan-pdf/', scan_pdf, name='scan_pdf'),
]

# Serving media files during development
from django.conf import settings
from django.conf.urls.static import static

# Include this only if you're in development mode and want to serve media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)