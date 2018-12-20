from django.shortcuts import render, redirect
from core.models import Quiz, Card
from core.forms import QuizForm, CardForm


# Create your views here.
def index(request):
    quizzes = Quiz.objects.all()
    return render(request, "index.html", {
        'quizzes': quizzes,
    })

def account(request):
    return render(request, "account.html")

def quiz_detail(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    cards = quiz.cards.all()
    return render(request, 'quizzes/quiz_detail.html', {
        'quiz': quiz,
        'cards': cards,
    })

def new_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.author = request.user
            quiz.save()
            return redirect('home')
    else:
        form = QuizForm()

    return render(request, 'quizzes/new_quiz.html', {

        "form": form,
    })

def new_card(request, pk):
    this_quiz = Quiz.objects.get(pk=pk)
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.quiz = this_quiz
            card.save()
            return redirect('quiz_detail', pk=this_quiz.pk)

    else:
        form = CardForm()

    return render(request, 'quizzes/add_card.html', {

        "form": form,
        "this_quiz": this_quiz

    })


def play_quiz(request):
    return render(request, 'quiz_play.html', {})