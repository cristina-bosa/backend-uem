from django.urls import path
from .views import (
    BeingTypeListCreate,
    BeingTypeRetrieveUpdateDestroy,


    BeingListCreate,
    BeingRetriveUpdateDestroy,

    StoryListCreate,
    StoryRetrieveUpdateDestroy,
    StoryFilter,
    
    HouseListCreate,
    HouseRetrieveUpdateDestroy,
)

urlpatterns = [
    path("being-type", BeingTypeListCreate.as_view(), name="being_type_list_create"),
    path("being-type/<int:pk>", BeingTypeRetrieveUpdateDestroy.as_view(), name="being_type_retrieve_update_destroy"),

    path("being/", BeingListCreate.as_view(), name="being_list_create"),
    path("being/<int:pk>", BeingRetriveUpdateDestroy.as_view(), name="being_retrieve_update_destroy"),

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
