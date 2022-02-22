from operator import mod
from django.db import models

# Create your models here.
class ParkItSpaceProvider(models.Model):
    """Park It Space Provider model."""
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    space_available_for = models.CharField(max_length=100)
    cost = models.IntegerField()
    city = models.CharField(max_length=100, default="")
    area = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name