from django.db import models
from django.db.models import Model

# Create your models here.
class Farm(Model):
    farm_name = models.CharField(max_length=50)
    city = models.CharField(max_length=255, blank=True, null=True)
    farm_location = models.CharField(max_length=50)
    prediction = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.farm_name