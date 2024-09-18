from django.db import models
from account.models import User


class BloodDonationRequest(models.Model):
    REQUEST_TYPE_CHOICES = [('donating', 'Donating'), ('looking', 'Looking')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=10, choices=REQUEST_TYPE_CHOICES)
    blood_type = models.CharField(max_length=3)
    region = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.request_type}'