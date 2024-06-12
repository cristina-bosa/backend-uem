from django.db import models


class ProjectStatus(models.TextChoices):
    ACTIVE = 'Active'
    IN_PROGRESS = 'In Progress'
    DELETED = 'Deleted'
    FINISHED = 'Finished'


class TaskStatus(models.TextChoices):
    TODO = 'To Do'
    DOING = 'Doing'
    DONE = 'Done'

