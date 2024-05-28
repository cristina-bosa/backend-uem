from rest_framework import serializers
from ..models import BeingType


class BeingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeingType
        fields = "__all__"
