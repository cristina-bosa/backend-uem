from rest_framework import generics
from ..serializers import BeingSerializer
from ..models import Being


class BeingListCreate(generics.ListCreateAPIView):
    queryset = Being.objects.all()
    serializer_class = BeingSerializer


class BeingRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Being.objects.all()
    serializer_class = BeingSerializer