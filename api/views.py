from core.models import Quiz, Card
from rest_framework import viewsets
from api.serializers import QuizSerializer, CardSerializer
from django.shortcuts import render

# Create your views here.

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
