from core.models import User, Quiz, Card
from api.serializers import UserSerializer, QuizSerializer, CardSerializer
from rest_framework import generics

class QuizListCreateView(generics.ListCreateAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        return self.request.user.quizzes

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)