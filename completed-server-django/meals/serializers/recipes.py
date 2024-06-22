from rest_framework import serializers

from meals.models.recipes import Recipes
from meals.serializers.recipes_ingredients import RecipesIngredientsSerializer


class RecipesSerializers(serializers.ModelSerializer):
    ingredients = RecipesIngredientsSerializer(many=True, read_only = True)
    class Meta:
        model = Recipes
        fields = '__all__'
