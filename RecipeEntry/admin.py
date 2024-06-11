from django.contrib import admin
from .models import Recipe,Steps, RecipeIngredient

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Steps)
admin.site.register(RecipeIngredient)
