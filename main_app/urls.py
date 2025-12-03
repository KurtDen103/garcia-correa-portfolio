# main_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Palitan ang 'home' ng pangalan ng function mo sa views.py
]