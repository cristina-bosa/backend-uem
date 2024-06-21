from django.urls import path
from rest_framework import routers
#
from meals.views.categories import CategoriesListCreate, CategoriesRetrieveUpdateDestroy
from meals.views.ingredients import IngredientsListCreate, IngredientsRetrieveUpdateDestroy
from meals.views.rating import RatingViewSet
from meals.views.recipes import RecipesViewSet
from meals.views.top_recipes import TopRecipesView

router = routers.DefaultRouter()
router.register(r'api/recipes', RecipesViewSet, basename='recipes')
router.register(r'api/rating', RatingViewSet, basename='rating')
router.urlpatterns = router.urls
router.urlpatterns += [
    path('api/top-recipes/', TopRecipesView.as_view(), name='top_recipes'),
    path('api/categories/', CategoriesListCreate.as_view(), name='list_create_categories'),
    path('api/categories/<int:pk>/', CategoriesRetrieveUpdateDestroy.as_view(), name='retrieve_update_categories'),
    path('api/ingredients/', IngredientsListCreate.as_view(), name='list_create_ingredients'),
    path('api/ingredients/<int:pk>/', IngredientsRetrieveUpdateDestroy.as_view(), name='retrieve_update_ingredients'),
    ]
