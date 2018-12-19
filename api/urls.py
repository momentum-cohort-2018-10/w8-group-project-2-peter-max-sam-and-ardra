from django.urls import path
from api import views as api_views

urlpatterns = [
    path("quizzes/", api_views.QuizListCreateView.as_view(), name="quiz-list"),
]