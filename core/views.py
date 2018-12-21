from django.shortcuts import render, redirect
from core.models import Quiz, Card
from core.forms import QuizForm, CardForm
# from django.url import reverse


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

    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.quiz = quiz
            card.save()
            # return redirect('home')
            return redirect('quiz_detail', pk=quiz.pk)

    else:
        form = CardForm()


    return render(request, 'quizzes/quiz_detail.html', {
        'quiz': quiz,
        'cards': cards,
        'form': form,
    })

def delete_card(request, pk):
    """deletes a users card, user must be logged in"""
    
    card = Card.objects.get(pk=pk)
    quiz_id = card.quiz.id
    # if (request.user == quiz.author) or (request.user.is_staff):
    card.delete()
    return redirect('quiz_detail', pk=quiz_id)
    # return render(request, 'quizzes/quiz_detail.html',)

def delete_quiz(request, pk):
    """deletes a users quiz, user must be logged in"""
    # quiz = Quiz.objects.get(pk=pk)
    quiz = Quiz.objects.get(pk=pk)
    # if (request.user == quiz.author) or (request.user.is_staff):
    quiz.delete()
    return redirect('home')
    # return render(request, 'quizzes/quiz_detail.html',)

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

# def new_card(request, pk):
#     this_quiz = Quiz.objects.get(pk=pk)
#     cards = this_quiz.cards.all()

#     if request.method == 'POST':
#         form = CardForm(request.POST)
#         if form.is_valid():
#             card = form.save(commit=False)
#             card.quiz = this_quiz
#             card.save()
#             return redirect('home')
#             # return redirect('quiz_detail', pk=this_quiz.pk)

#     else:
#         form = CardForm()

#     return render(request, 'quizzes/quiz_detail.html', {

#         "form": form,
#         "this_quiz": this_quiz,
#         "cards": cards,

#     })

def take_quiz(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    card_list = quiz.cards.all()
    card = card_list.first()

    return render(request, 'quizzes/quiz.html', {
        'quiz': quiz,
        'card_list': card_list,
        'card': card,
    })

