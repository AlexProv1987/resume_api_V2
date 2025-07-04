"""
URL configuration for resume_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/applicant/", include("api.applicant.urls")),
    path("api/details/", include("api.applicant_details.urls")),
    path("api/work/", include("api.work_details.urls")),
    path("api/projects/", include("api.projects.urls")),
    path("api/feedback/",include("api.feedback.urls")),
    path("api/question/",include("api.question.urls")),
]
