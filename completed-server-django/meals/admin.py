from django.contrib import admin

from meals.models.rating import Rating
from meals.models.recipes import Recipes
from meals.models.recipes_ingredients import RecipesIngredients
from meals.models.categories import Categories
from meals.models.ingredients import Ingredients

# Register your models here.
admin.register({
    Categories,
    Ingredients,
    Recipes,
    RecipesIngredients,
    Rating,
    })
