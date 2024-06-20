from rest_framework import viewsets

from meals.models.rating import Rating
from meals.serializers.rating import RatingSerializers


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers

