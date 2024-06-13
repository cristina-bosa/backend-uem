from django.db import models

from .status import ProjectStatus


class Projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255, choices = ProjectStatus.choices, default = ProjectStatus.ACTIVE,
                              blank = True)
    start_date = models.DateTimeField(null = True)
    end_date = models.DateTimeField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name
