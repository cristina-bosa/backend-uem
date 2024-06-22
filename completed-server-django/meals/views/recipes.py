from http import HTTPStatus

from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from meals.models.recipes import Recipes
from meals.models.recipes_ingredients import RecipesIngredients
from meals.serializers.recipes import RecipesSerializers


class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializers

    def create(self, request, *args, **kwargs):
        request.data['owner'] = request.user.id
        response = super().create(request, *args, **kwargs)
        return response

    @action(detail = True, methods = ['post'], url_path = 'add-ingredients', permission_classes = [
        permissions.IsAuthenticated])
    def add_ingredients(self, request, pk):
        recipe = self.queryset.get(pk = pk)
        ingredients = request.data.get('ingredients')
        for ingredient in ingredients:
            ingredient_id = ingredient.get('ingredient')
            quantity = ingredient.get('quantity')
            try:
                RecipesIngredients.objects.create(
                        recipe = recipe,
                        ingredient_id = ingredient_id,
                        quantity = quantity,
                        )
            except Exception as e:
                pass
        return Response(self.serializer_class(recipe).data, status = HTTPStatus.OK)

    @action(detail = True, methods = ['post'], url_path = 'delete-ingredients', permission_classes = [
        permissions.IsAuthenticated])
    def delete_ingredients(self, request, pk):
        recipe = self.queryset.get(pk = pk)
        ingredients = request.data.get('ingredients')
        RecipesIngredients.objects.filter(
                recipe = recipe,
                ingredient_id__in = ingredients
                ).delete()
        return Response(self.serializer_class(recipe).data, status = HTTPStatus.OK)

    @action(detail=False, methods=['get'], url_path = 'me', permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        recipes = self.queryset.filter(owner=request.user)
        return Response(RecipesSerializers(recipes, many = True).data)
