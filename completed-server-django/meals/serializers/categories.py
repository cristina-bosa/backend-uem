from rest_framework import serializers

from meals.models.categories import Categories


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
