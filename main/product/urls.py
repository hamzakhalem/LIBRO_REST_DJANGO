from django.contrib import admin
from django.urls import path
from .views import get_all_products, get_by_id_product
urlpatterns = [
    path('products/', get_all_products, name='products'),
    path('products/<str:pk>/', get_by_id_product, name='products'),
]