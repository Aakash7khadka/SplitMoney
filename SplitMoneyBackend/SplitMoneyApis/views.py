from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from . import serializers
from . import models
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_trips(request):
    trips = models.TripParticipants.objects.all()
    trips = models.TripParticipants.objects.filter(userId = request.user.email)
    print(request.user.id)
  
    serializer = serializers.TripParticipantsSerializer(trips, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def insert_trip(request):
    serializer = serializers.TripSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['POST'])
def insert_trip_participants(request):
    serializer = serializers.TripParticipantsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
def insert_expenses(request):
    serializer = serializers.ExpenseSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
