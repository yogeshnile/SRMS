from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result', views.result, name='result'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
]