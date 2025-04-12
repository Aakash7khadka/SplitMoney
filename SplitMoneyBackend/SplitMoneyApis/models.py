from django.db import models

# Create your models here.
class Trip(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=150)
    trip_date = models.DateField()
    created_date = models.DateField(auto_now_add=True, null=True)
    updated_date = models.DateField(auto_now_add=True, null=True)


    def __str__(self):
        return self.location


class TripParticipants(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.CharField(max_length=150)
    tripId = models.ForeignKey(Trip, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True, null=True)
    updated_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.id