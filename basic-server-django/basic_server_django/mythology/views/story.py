from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class StoryView(APIView):
    def get(self, request):
        return Response({}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({}, status=status.HTTP_201_CREATED) 
                        
# class BeingTypeListCreate(APIView):
#     def get(self, request):
#         being_types = BeingType.objects.all()
#         serializer = BeingTypeSerializer(being_types, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = BeingTypeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BeingTypeRetrieveUpdateDestroy(APIView):

#     def __get_one(self, id):
#         try:
#             return BeingType.objects.get(id=id)
#         except BeingType.DoesNotExist:
#             return None

#     def get(self, request, id):
#         being_type = self.__get_one(id)
#         if being_type:
#             serializer = BeingTypeSerializer(being_type)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({}, status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, id):
#         being_type = self.__get_one(id)
#         if being_type:
#             being_type.delete()
#             return Response({}, status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response({}, status=status.HTTP_404_NOT_FOUND)

#     def put(self, request, id):
#         being_type = self.__get_one(id)
#         if being_type:
#             serializer = BeingTypeSerializer(being_type, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({}, status=status.HTTP_200_OK)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response({}, status=status.HTTP_404_NOT_FOUND)
