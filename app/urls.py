from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.TaskViews.as_view()),
    path("tasks/<int:id>", views.TaskViews.as_view()),
]
