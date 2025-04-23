from django.urls import path
from .views import check_pdf

urlpatterns = [
    path('check-pdf/', check_pdf, name='check_pdf'),
]
