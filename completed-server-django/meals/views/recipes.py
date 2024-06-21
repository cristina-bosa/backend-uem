from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from meals.models.recipes import Recipes
from meals.serializers.recipes import RecipesSerializers


class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializers

    def create(self, request, *args, **kwargs):
        request.data['owner'] = request.user.id
        response = super().create(request, *args, **kwargs)
        return response

    def update(self, request, *args, **kwargs):

        return super().update(request, *args, **kwargs)

    @action(detail = True, methods = ['post'], url_path = 'add-ingredients', permission_classes = [
        permissions.IsAuthenticated])
    def add_ingredients(self, request):
        recipes = self.queryset.filter(owner = request.user)
        return Response(RecipesSerializers(recipes, many = True).data)

    @action(detail = True, methods = ['post'], url_path = 'delete-ingredients', permission_classes = [
        permissions.IsAuthenticated])
    def delete_ingredients(self, request):
        recipes = self.queryset.filter(owner = request.user)
        return Response(RecipesSerializers(recipes, many = True).data)

    @action(detail=True, methods=['get'], url_path = 'me', permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        recipes = self.queryset.filter(owner=request.user)
        return Response(RecipesSerializers(recipes, many = True).data)
