
from . import models
from rest_framework import serializers

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Trip
        fields = '__all__'
        read_only_fields = ['created_date']


class TripParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TripParticipants
        read_only_fields = ['created_date']
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Expenses
        fields = '__all__'
        extra_kwargs = {'payer_id': {'required': False}}