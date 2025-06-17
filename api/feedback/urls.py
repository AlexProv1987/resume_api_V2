from . import views
from django.urls import path

urlpatterns = [
    path("create/", views.CreateFeedBack.as_view()),
]
