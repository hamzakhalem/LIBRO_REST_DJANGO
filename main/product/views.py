from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import PoductSerializer
from .filters import ProductFilter
# Create your views here.

@api_view(['GET'])
def get_all_products(request):
    filterset = ProductFilter(request.GET, queryset=Product.objects.all())
    serializer = PoductSerializer(filterset.qs, many=True)
    return Response({'product': serializer.data})

@api_view(['GET'])
def get_by_id_product(request, pk):
    products = get_object_or_404(Product, id=pk)
    serializer = PoductSerializer(products, many=False)
    return Response({'product': serializer.data})