from django.db import models
from Inventory.models import Ingredient

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length= 255)
    image = models.ImageField(upload_to='recipes/')
    description = models.TextField(max_length=255)
    def __str__(self):
        return self.name

class Steps (models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    stepId = models.IntegerField(primary_key=True)
    stepImage = models.ImageField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.Recipe} - {self.description}'
    
    class Meta:
        verbose_name_plural = 'Steps'

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits= 10,decimal_places=2)
    unit = models.CharField(max_length=50)
    