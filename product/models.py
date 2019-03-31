from django.db import models

# Create your models here.
class Mobile(models.Model):
    name  = models.CharField(max_length=100)
    specs = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=10000)
