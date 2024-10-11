from django.shortcuts import render, get_object_or_404
from django.db.models import Avg

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Order, OrderItem
from .serializers import  OrderItemSerializer, OrderSerializer
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def newOrder(request):
    user = request.user
    data = request.data
    order_items =  data['order_items']
    serializer = OrderSerializer(data=data, many=False)
    if serializer.is_valid():
        order = Order.objects.create(**data, user=request.user)
        res = OrderSerializer(order, many=False)
        return Response({'order': res})
    else:
        return Response({'order': serializer.errors})
    