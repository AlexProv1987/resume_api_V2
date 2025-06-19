from . import views
from django.urls import path

urlpatterns = [
    path("ask/", views.AskQuestion.as_view()),
]
