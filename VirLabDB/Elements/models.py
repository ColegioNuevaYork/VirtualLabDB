from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=255)
    uncertainty = models.DecimalField(max_digits=100, decimal_places=2)
    brand = models.CharField(blank=True, max_length=255)
    quantity = models.DecimalField(max_digits=100, decimal_places=2)
    Available = models.BooleanField(default=True)
