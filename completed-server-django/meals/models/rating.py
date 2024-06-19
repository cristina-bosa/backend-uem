from django.db import models


class Rating(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    recipe = models.ForeignKey('Recipes', on_delete=models.CASCADE)
    value = models.IntegerField()

    class Meta:
        unique_together = ('user', 'meal')