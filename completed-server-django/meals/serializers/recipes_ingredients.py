from rest_framework import serializers

from meals.models.recipes_ingredients import RecipesIngredients


class RecipesIngredientsSerializer(serializers.ModelSerializer):
    ingredient = serializers.CharField(source='name', read_only=True)
    class Meta:
        model = RecipesIngredients
        fields = ['ingredient', 'quantity']