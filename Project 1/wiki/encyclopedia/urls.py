from django.urls import path

from . import views

app_name = "wikipedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("random", views.randomPage,name="random"),
    path("<str:name>", views.entry, name="entry"),
    path("edit/<str:name>", views.edit, name="edit")
]