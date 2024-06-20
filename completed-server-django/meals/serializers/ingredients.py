from rest_framework import serializers

from meals.models.ingredients import Ingredients


class IngredientsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'
