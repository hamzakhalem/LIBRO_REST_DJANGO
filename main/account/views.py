from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .serializers import SignUpSerializer, UserSerializer
# Create your views here.


@api_view(['POST'])
def regiser(request):
    data = request.data
    user = SignUpSerializer(data = data)

    if user.is_valid():
        if not User.objects.filter(username=data['email']).exists:
            user = User.objects.create(
            )
