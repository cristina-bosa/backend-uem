from rest_framework import generics
from ..serializers import BeingTypeSerializer
from ..models import BeingType


class BeingTypeCreate(generics.CreateAPIView):
    queryset = BeingType.objects.all()
    serializer_class = BeingTypeSerializer


class BeingTypeList(generics.ListAPIView):
    queryset = BeingType.objects.all()
    serializer_class = BeingTypeSerializer


class BeingTypeRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = BeingType.objects.all()
    serializer_class = BeingTypeSerializer


class BeingTypeDestroy(generics.DestroyAPIView):
    queryset = BeingType.objects.all()
    serializer_class = BeingTypeSerializer