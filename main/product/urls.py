from django.contrib import admin
from django.urls import path
from .view import get_all_products
urlpatterns = [
    path('products/', get_all_products, name='products')
]