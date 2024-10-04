from django.contrib import admin
from django.urls import path
from .views import get_all_products, get_by_id_product, newProduct, updateProduct, deleteProduct
urlpatterns = [
    path('products/', get_all_products, name='products'),
    path('products/new/', newProduct, name='new-products'),
    path('products/<str:pk>/', get_by_id_product, name='products'),
    path('products/update/<str:pk>/', updateProduct, name='products'),
    path('products/delete/<str:pk>/', deleteProduct, name='products'),
]