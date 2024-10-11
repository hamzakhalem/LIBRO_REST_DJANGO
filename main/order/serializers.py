from rest_framework import serializers
from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    orderItems = serializers.SerializerMethodField(method_name='get_order_items', read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
#         # fields = ('name', 'price', 'brand')

    def get_order_items(self, obj):
        orderitems = obj.order_items.all()
        serializer = OrderItemSerializer(orderitems, many=True)
        return serializer.data
    
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'