from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import PoductSerializer
# Create your views here.

@api_view(['GET'])
def get_all_products(request):
    products = Product.objects.all()
    serializer = PoductSerializer(products, many=True)
    return Response({'product': serializer.data})