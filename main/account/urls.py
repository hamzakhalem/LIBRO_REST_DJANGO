from django.contrib import admin
from django.urls import path
from .views import regiser
urlpatterns = [
    path('register/', regiser, name='register'),
]