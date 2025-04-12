from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
import requests

@api_view(['POST'])
def register_user(request):
    """Registers a new user"""
    email = request.data.get('email')
    password = request.data.get('password')

    if User.objects.filter(email=email).exists():
        return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

    User.objects.create(email=email, password=make_password(password))
    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    """Logs out user by blacklisting refresh token"""
    try:
        refresh_token = request.data.get('refresh')
        RefreshToken(refresh_token).blacklist()
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
    except Exception:
        return Response({'error': 'Invalid refresh token'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    """Example protected view"""
    return Response({'message': f'Hello, {request.user.username}!'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def make_request(request):
    access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQzNzA1OTI4LCJpYXQiOjE3NDM3MDIzMjgsImp0aSI6IjRjMjE0ZWZmYzQ0NzQzYWVhYjllMDRiNTRmMzAxZjk2IiwidXNlcl9pZCI6MX0.vkQA-5Tn5OzWr6KZwb-CH6yN8EeBLUZLqhwkxSKeEUU'
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get("http://127.0.0.1:8000/api/protected/", headers=headers)

    if response.status_code == 200:
        try:
            return Response(response.json())  # Returns the JSON response if successful
        except ValueError:
            return Response({"error": "Invalid JSON response from the API"}, status=500)
    else:
        return Response({"error": "Failed to fetch protected resource", "status_code": response.status_code}, status=response.status_code)