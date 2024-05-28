from rest_framework import generics
from ..serializers import BeingSerializer
from ..models import Being


class BeingCreate(generics.CreateAPIView):
    queryset = Being.objects.all()
    serializer_class = BeingSerializer


class BeingList(generics.ListAPIView):
    queryset = Being.objects.all()
    serializer_class = BeingSerializer


class BeingRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Being.objects.all()
    serializer_class = BeingSerializer


class BeingDestroy(generics.DestroyAPIView):
    queryset = Being.objects.all()
    serializer_class = BeingSerializer
