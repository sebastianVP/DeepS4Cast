# core_forecast/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Esta será la página principal de tu dashboard
    path('', views.dashboard_estatico, name='dashboard'),
]