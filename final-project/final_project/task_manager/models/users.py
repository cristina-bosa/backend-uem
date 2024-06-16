from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    is_staff = None
    id_telegram = models.IntegerField(null = True, blank = True)
    def __str__(self):
        return self.username
