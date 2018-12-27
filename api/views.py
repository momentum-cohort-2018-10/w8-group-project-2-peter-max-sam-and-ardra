from core.models import Quiz, Card
from rest_framework import viewsets
from api.serializers import QuizSerializer, CardSerializer
from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.right_answers = request.data.get("right_answers")
        instance.save()

        return Response(serializer.data)
