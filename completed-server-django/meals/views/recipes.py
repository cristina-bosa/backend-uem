from rest_framework import viewsets

from meals.models.recipes import Recipes
from meals.serializers.recipes import RecipesSerializers


class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializers
