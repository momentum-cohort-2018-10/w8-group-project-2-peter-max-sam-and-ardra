from django.shortcuts import render
from core.models import Quiz, Card

# Create your views here.
def index(request):
    quizzes = Quiz.objects.all()
    return render(request, "index.html", {
        'quizzes': quizzes,
    })

def account(request):
    return render(request, "account.html")

def quiz_detail(request, slug):
    quiz = Quiz.objects.get(slug=slug)
    return render(request, 'quizzes/quiz.html', {
        'quiz': quiz,
    })
