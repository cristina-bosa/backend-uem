from django.db import models

from .status import TaskStatus


class Tasks(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255, choices = TaskStatus.choices, default = TaskStatus.TODO, blank = True)
    start_date = models.DateTimeField(null = True)
    end_date = models.DateTimeField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey('Projects', on_delete=models.CASCADE)
    users = models.ManyToManyField('Users')

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.name
