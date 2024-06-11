from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse

from RecipeEntry.models import *



# Create your views here.
def index(request):
    latest_recipes = get_list_or_404(Recipe.objects)
    template = loader.get_template('RecipeEntry/index.html')
    context = {
        "latest_recipe_list": latest_recipes,
    }
    return HttpResponse(template.render(context, request))


def detail(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    return render(request, "RecipeEntry/detail.html", {"recipe": recipe})

def newEntry(request):
    return render(request,'RecipeEntry/entry.html')