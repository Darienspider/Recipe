from django.contrib import admin
from django.urls import path
from .views import index,detail, newEntry

app_name = 'RecipeEntry'
urlpatterns = [
    path('',view=index, name='index'),
    path('<int:recipe_id>/', view = detail, name='details' ),
    path('new/',view =newEntry, name ='entry' )
]
