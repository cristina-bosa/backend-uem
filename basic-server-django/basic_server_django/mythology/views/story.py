from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import StorySerializer
from ..models import Story


class StoryListCreate(APIView):
    def get(self, request):
        story = Story.objects.all()
        serializer = StorySerializer(story, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        story = Story.objects.all()
        serializer = StorySerializer(story, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoryRetrieveUpdateDestroy(APIView):
    def __get_one(self, pk):
        try:
            return Story.objects.get(pk=pk)
        except Story.DoesNotExist:
            return None

    def get(self, request, pk):
        story = self.__get_one(pk)
        if story:
            serializer = StorySerializer(story)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        story = self.__get_one(pk)
        if story:
            story.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        story = self.__get_one(pk)
        if story:
            serializer = StorySerializer(story, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_404_NOT_FOUND)
