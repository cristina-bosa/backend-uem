from django.db import models


class BeingType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True)    

    class Meta:
        ordering = ["name"]
        verbose_name = "being_type"
        verbose_name_plural = "being_types"

    def __str__(self):
        return self.name