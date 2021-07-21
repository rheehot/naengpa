from .models import Recipe
from rest_framework import serializers

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('name','time','need_ingredient','content','create_date')
