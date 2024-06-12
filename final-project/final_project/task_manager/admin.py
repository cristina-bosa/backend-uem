from django.contrib import admin
from .models import Users
from .models.comments import Comments
from .models.projects import Projects
from .models.tasks import Tasks

# Register your models here.
admin.register({Projects, Tasks, Users, Comments})
