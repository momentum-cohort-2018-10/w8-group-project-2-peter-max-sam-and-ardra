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

    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.quiz = quiz
            card.save()
            messages.success(request, 'Card Added')
            return redirect('quiz_detail', pk=quiz.pk)
        else:
            messages.warning(request, 'Sorry, something did not work. Make sure you fill out both question and answer fields.')

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
def play_quiz(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quiz_play.html', {
        'quiz': quiz,
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

# def take_quiz(request, pk):
#     quiz = Quiz.objects.get(pk=pk)
#     card_list = quiz.cards.all()
#     card = card_list.first()

def edit_quiz(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    form_class = QuizForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            return redirect("quiz_detail", pk=quiz.pk)
    
    else:
        form = form_class(instance=quiz)
    return render(request, 'quizzes/edit_quiz.html', {'quiz': quiz, 'form': form, })


def edit_card(request, pk):
    card = Card.objects.get(pk=pk)
    form_class = CardForm
    if request.method =='POST':
        form = form_class(data=request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('quiz_detail', pk=card.pk)

    else:
        form = form_class(instance=card)
    return render(request, 'cards/edit_card.html', {'card': card, 'form': form, })
