from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Product
from .serializers import PoductSerializer
from .filters import ProductFilter
# Create your views here.

@api_view(['GET'])
def get_all_products(request):
    filterset = ProductFilter(request.GET, queryset=Product.objects.all())
    count = filterset.qs.count()
    resPage = 1
    paginator = PageNumberPagination() 
    paginator.page_size = resPage
    queryset = paginator.paginate_queryset(filterset.qs, request)
    serializer = PoductSerializer(queryset, many=True)
    return Response({'product': serializer.data, 'perpage': resPage, 'total': count })

@api_view(['GET'])
def get_by_id_product(request, pk):
    products = get_object_or_404(Product, id=pk)
    serializer = PoductSerializer(products, many=False)
    return Response({'product': serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def newProduct(request):
    data = request.data
    serializer = PoductSerializer(data=data, many=False)
    if serializer.is_valid():
        product = Product.objects.create(**data, user=request.user)
        res = PoductSerializer(product, many=False)
        return Response({'product': res})
    else:
        return Response({'product': serializer.errors})
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProduct(request, pk):
    product = get_object_or_404(Product, id=pk)

    data = request.data
    if product.user != request.user:
        return Response({'error': "you cant update"}, status= status.HTTP_403_FORBIDDEN)
    
    product.name = data['name']
    product.description = data['description']
    product.price = data['price']
    product.brand = data['brand']
    product.ratings = data['ratings']
    product.stock = data['stock']
    product.save()
    serializer = PoductSerializer(product, many=False)
    
    return Response({'product': serializer.data})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteProduct(request, pk):
    product = get_object_or_404(Product, id=pk)

    data = request.data
    if product.user != request.user:
        return Response({'error': "you cant update"}, status= status.HTTP_403_FORBIDDEN)
    
    product.delete()
    serializer = PoductSerializer(product, many=False)
    
    return Response({'product': "deleted"}, status=status.HTTP_200_OK)


