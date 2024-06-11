from django.contrib import admin
from django.urls import path
from .views import index,detail

app_name = 'RecipeEntry'
urlpatterns = [
    path('',view=index, name='index'),
    path('<int:recipe_id>/', view = detail, name='details' )
]
