from . import views
from django.urls import path

urlpatterns = [
    path("get_projects/", views.GetProjects.as_view()),
    path("project_details/", views.GetProjectDetails.as_view()),
]
