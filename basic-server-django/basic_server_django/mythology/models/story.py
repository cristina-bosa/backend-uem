from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        ordering = ["title"]
        verbose_name = "story"
        verbose_name_plural = "stories"

    def __str__(self):
        return self.title
