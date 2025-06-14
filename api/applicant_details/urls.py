from . import views
from django.urls import path

urlpatterns = [
    path("skills/", views.GetApplicantSkills.as_view()),
    path("education/", views.GetApplicantEducation.as_view()),
    path("certifications/", views.GetApplicantCertifications.as_view()),
    path("references/", views.GetApplicantReferences.as_view()),
    path("added_context/", views.GetApplicantAdditionalContext.as_view()),
]
