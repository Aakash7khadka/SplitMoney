from django.db import models
from Authentication.models import User

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


class Expenses(models.Model):
    id = models.AutoField(primary_key=True)
    payer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    payer_email = models.CharField(max_length=200)
    trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=300, null=True)
    created_date = models.DateField(auto_now_add=True, null=True)
    updated_date = models.DateField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        self.payer_id = User.objects.get(email = self.payer_email)
        super().save(*args, **kwargs)