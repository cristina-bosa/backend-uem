from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import HouseSerializer
from ..models import House


class HouseListCreate(APIView):
    def get(self, request):
        house = House.objects.all()
        serializer = HouseSerializer(house, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        house = House.objects.all()
        serializer = HouseSerializer(house, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HouseRetrieveUpdateDestroy(APIView):
    def __get_one(self, pk):
        try:
            return House.objects.get(pk=pk)
        except House.DoesNotExist:
            return None

    def get(self, request, pk):
        house = self.__get_one(pk)
        if house:
            serializer = HouseSerializer(house)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        house = self.__get_one(pk)
        if house:
            house.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        house = self.__get_one(pk)
        if house:
            serializer = HouseSerializer(house, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_404_NOT_FOUND)
