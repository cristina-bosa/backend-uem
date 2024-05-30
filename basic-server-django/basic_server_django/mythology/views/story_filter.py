from os import name
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import StorySerializer
from ..models import Story
from ..models import BeingType
from ..models import Being
from ..models import House


class StoryFilter(APIView):
    def get(self, request):
        data = request.data
        stories = Story.objects.all()

        if "house" in data and data["house"]:
            house = House.objects.filter(name__icontains=data["house"])
            stories = stories.filter(being__house__in=house)

        if "being_type" in data and data["being_type"]:
            being_type = BeingType.objects.filter(name__icontains=data["being_type"])
            stories = stories.filter(being__type__in=being_type)

        if "being" in data and data["being"]:
            being = Being.objects.filter(name__icontains=data["being"])
            stories = stories.filter(being__in=being)

        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
