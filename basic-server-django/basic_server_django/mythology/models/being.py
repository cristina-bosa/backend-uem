from django.db import models
from .being_type import BeingType
from .house import House
from .story import Story


class Being(models.Model):
    name = models.CharField(max_length=100)
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(BeingType, on_delete=models.CASCADE)
    story = models.OneToOneField(Story, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]
        verbose_name = "being"
        verbose_name_plural = "beings"

    def __str__(self):
        return self.name
