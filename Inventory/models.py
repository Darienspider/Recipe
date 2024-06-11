from django.db import models

# Create your models here.
class Ingredient (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits= 10, decimal_places=2)
    lastPurchased = models.DateTimeField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return (self.name)

