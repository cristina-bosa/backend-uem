from django.db import models


class RecipesIngredients(models.Model):
    quantity = models.FloatField()
    recipe = models.ForeignKey('Recipes', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredients', on_delete=models.CASCADE)

    class Meta:
        ordering = ['recipe']
        verbose_name = 'recipe_ingredient'
        verbose_name_plural = 'recipes_ingredients'

    def __str__(self):
        return f'{self.recipe.name} - {self.ingredient.name}'