from django.contrib import admin
from .models import BeingType, Being, Story

admin.register({BeingType, Being, Story})