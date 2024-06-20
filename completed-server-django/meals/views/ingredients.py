from rest_framework import generics

from meals.models.ingredients import Ingredients
from meals.serializers.ingredients import IngredientsSerializers


class IngredientsListCreate(generics.ListCreateAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializers


class IngredientsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializers
