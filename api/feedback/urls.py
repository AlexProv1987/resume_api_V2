from . import views
from django.urls import path

urlpatterns = [
    path("create/feedback", views.CreateFeedBack.as_view()),
    path("create/llmresponse",views.StoreLLMResponse.as_view()),
]
