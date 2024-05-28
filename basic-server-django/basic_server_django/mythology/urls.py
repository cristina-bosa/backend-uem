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
    StoryView,
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
    )
]
