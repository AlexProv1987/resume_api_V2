from . import views
from django.urls import path

urlpatterns = [
    path("get_applicant/<str:pk>", views.GetApplicant.as_view()),
    path("get_resume/<str:pk>",views.GetResume.as_view()),
    path('applicant_set/<str:pk>',views.GetApplicantSet.as_view()),
]
