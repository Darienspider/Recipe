from django.db import models

# Create your models here.
class Recipe(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length= 255)
    
    def __str__(self):
        return self.name

class Steps (models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    stepId = models.IntegerField(primary_key=True)
    stepImage = models.ImageField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.Recipe} - {self.description}'
