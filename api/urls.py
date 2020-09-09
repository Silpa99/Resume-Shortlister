from django.urls import path
from api.views import QuestionView

urlpatterns = [
    path('questions', QuestionView.as_view()),
]