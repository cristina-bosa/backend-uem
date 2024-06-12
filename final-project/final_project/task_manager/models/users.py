from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    is_staff = None

    def __str__(self):
        return self.username
