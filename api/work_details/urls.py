from . import views
from django.urls import path

urlpatterns = [
    path("history/", views.GetApplicantWorkHistory.as_view()),
    path("history_details/", views.GetWorkHistoryDetails.as_view()),
]
