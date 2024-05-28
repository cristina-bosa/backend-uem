from django.db import models
from .being_type import BeingType


class Being(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.ForeignKey(BeingType, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]
        verbose_name = "being"
        verbose_name_plural = "beings"

    def __str__(self):
        return self.name
