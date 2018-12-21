from django.shortcuts import render, redirect
from core.models import Quiz, Card
from core.forms import QuizForm, CardForm
from django.contrib import messages


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
            messages.success(request, 'A new quiz has been made! Now add some cards.')
            return redirect('home')
        else:
            messages.warning(request, 'Sorry, something went wrong. Please try again!')
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
            messages.success(request, 'On your way to learning! Would you like to add more cards?')
            return redirect('quiz_detail', pk=this_quiz.pk)
        else:
            messages.warning(request, 'Sorry, something did not work. Make sure you fill out both question and answer fields.')

    else:
        form = CardForm()

    return render(request, 'quizzes/add_card.html', {

        "form": form,
        "this_quiz": this_quiz

    })
