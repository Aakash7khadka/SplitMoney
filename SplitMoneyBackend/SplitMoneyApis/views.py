from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from . import models
# Create your views here.


@api_view(['GET'])
def get_all_trips(request):
    trips = models.Trip.objects.all()
    serializer = serializers.TripSerializer(trips, many=True)
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
