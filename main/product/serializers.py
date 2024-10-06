from rest_framework import serializers
from .models import Product, Review


class PoductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('name', 'price', 'brand')
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        # fields = ('name', 'price', 'brand')