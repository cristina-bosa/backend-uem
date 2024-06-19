from django.db import models


class RecipesIngredients(models.Model):
    recipe = models.ForeignKey('Recipes', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredients', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Recipe Ingredient'
        verbose_name_plural = 'Recipes Ingredients'

    def __str__(self):
        return f'{self.recipe.name} - {self.ingredient.name}'