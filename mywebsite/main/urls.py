from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("projects/<int:id>", views.details, name="details"),
]
