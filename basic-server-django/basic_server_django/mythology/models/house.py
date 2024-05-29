from django.db import models


class House(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "house"
        verbose_name_plural = "houses"

    def __str__(self):
        return self.name
