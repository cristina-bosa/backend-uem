from rest_framework import serializers

from meals.models.recipes import Recipes


class RecipesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = '__all__'
