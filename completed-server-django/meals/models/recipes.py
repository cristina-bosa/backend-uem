from django.db import models


class Recipes (models.Model):
    name = models.CharField(max_length=100)
    instructions = models.TextField()
    time = models.TimeField()
    difficulty = models.IntegerField()
    owner = models.ForeignKey('authentication.Users', on_delete=models.CASCADE)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'

    def __str__(self):
        return self.name
