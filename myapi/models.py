from django.db import models

# Create your models here.
class Rapper(models.Model):
    name = models.CharField(max_length=100)
    aka = models.CharField(max_length=60)
    def __str__(self):
        return self.aka

class Stock(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return self.name