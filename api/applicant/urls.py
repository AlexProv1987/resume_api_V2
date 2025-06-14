from . import views
from django.urls import path

urlpatterns = [
    path("get_applicant/<pk>", views.GetApplicant.as_view()),
]
