from rest_framework import generics
from ..serializers import BeingTypeSerializer
from ..models import BeingType


class BeingTypeListCreate(generics.ListCreateAPIView):
    queryset = BeingType.objects.all()
    serializer_class = BeingTypeSerializer


class BeingTypeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BeingType.objects.all()
    serializer_class = BeingTypeSerializer