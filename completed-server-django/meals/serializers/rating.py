from rest_framework import serializers

from meals.models.rating import Rating


class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
