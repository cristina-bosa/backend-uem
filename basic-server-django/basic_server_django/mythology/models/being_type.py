from django.db import models


class BeingType(models.Model):
    name = models.CharField(max_length=100)    

    class Meta:
        ordering = ["name"]
        verbose_name = "being_type"
        verbose_name_plural = "being_types"

    def __str__(self):
        return self.name
