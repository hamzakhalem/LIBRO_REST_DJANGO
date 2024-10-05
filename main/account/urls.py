from django.contrib import admin
from django.urls import path
from .views import regiser, current_user, update_user
urlpatterns = [
    path('register/', regiser, name='register'),
    path('userinfo/', current_user, name='user_info'),
    path('userinfo/update/', update_user, name='user_info'),
]