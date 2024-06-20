from rest_framework import generics

from meals.models.categories import Categories
from meals.serializers.categories import CategoriesSerializers


class CategoriesListCreate(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers


class CategoriesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers

