from django.db import models
from .being import Being


class Story(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    being = models.ForeignKey(Being, on_delete=models.CASCADE)

    class Meta:
        ordering = ["title"]
        verbose_name = "story"
        verbose_name_plural = "stories"

    def __str__(self):
        return self.title