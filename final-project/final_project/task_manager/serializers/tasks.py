from rest_framework import serializers

from ..models.tasks import Tasks


class TaskSerializer (serializers.ModelSerializer) :
    class Meta:
        model = Tasks
        fields = '__all__'
