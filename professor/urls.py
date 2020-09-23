from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.handellogin, name='handellogin'),
    path('', views.dashboard, name='dashboard'),
    path('logout', views.handellogout, name='handellogout'),
    path('result-upload', views.resultupload, name='resultupload'),
]
