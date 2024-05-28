from rest_framework import serializers
from ..models import Being


class BeingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Being
        fields = "__all__"
