from django.db import models

# Create your models here

class Product(models.Model):
    name=models.CharField(max_length=50)
    descripccion=models.CharField(max_length=400, default='Sin descripción')
    precio =models.DecimalField(max_digits=10, decimal_places=2, default='0.0')
    stock = models.PositiveIntegerField()


