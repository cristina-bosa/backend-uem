from django.urls import path
from .views import (
    BeingTypeCreate,
    BeingTypeList,
    BeingTypeRetrieveUpdate,
    BeingTypeDestroy,
    BeingCreate,
    BeingList,
    BeingRetrieveUpdate,
    BeingDestroy,
    StoryListCreate,
    StoryRetrieveUpdateDestroy,
    StoryFilter,
    HouseListCreate,
    HouseRetrieveUpdateDestroy,
)

urlpatterns = [
    path("being-type", BeingTypeList.as_view(), name="being_type_list"),
    path("being-type", BeingTypeCreate.as_view(), name="being_type_create"),
    path(
        "being-type/<int:pk>",
        BeingTypeRetrieveUpdate.as_view(),
        name="being_type_retrieve_update",
    ),
    path(
        "being-type/<int:pk>",
        BeingTypeDestroy.as_view(),
        name="being_type_destroy",
    ),
    path("being", BeingList.as_view(), name="being_list"),
    path("being", BeingCreate.as_view(), name="being_create"),
    path("being/<int:pk>", BeingRetrieveUpdate.as_view(), name="being_retrieve_update"),
    path("being/<int:pk>", BeingDestroy.as_view(), name="being_destroy"),
    path("story", StoryListCreate.as_view(), name="story_list_create"),
    path(
        "story/<int:pk>",
        StoryRetrieveUpdateDestroy.as_view(),
        name="story_retrieve_update_destroy",
    ),
    path("story-filter", StoryFilter.as_view(), name="story_filter"),
    path("house", HouseListCreate.as_view(), name="house_list_create"),
    path(
        "house/<int:pk>",
        HouseRetrieveUpdateDestroy.as_view(),
        name="house_retrieve_update_destroy",
    ),
]
