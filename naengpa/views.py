#from django.shortcuts import render
from .models import Recipe
from rest_framework import viewsets
from .serializers import RecipeSerializer
from django.shortcuts import render

# Create your views here.
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


def index(request):
    recipe_list = Recipe.objects.order_by('-create_date')
    context = {'recipe_list':recipe_list}
    return render(request,'naengpa/recipe_list.html',context)
