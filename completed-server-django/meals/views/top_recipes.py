from http import HTTPStatus

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from meals.models.rating import Rating
from meals.models.recipes import Recipes
from meals.serializers.recipes import RecipesSerializers
from django.db.models import Avg


# modelo recipes y rating


class TopRecipesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        top_recipes = Recipes.objects.annotate(rating_value=Avg('rating__value')).order_by('rating_value')
        return Response(RecipesSerializers(top_recipes, many=True).data, status=HTTPStatus.OK)
