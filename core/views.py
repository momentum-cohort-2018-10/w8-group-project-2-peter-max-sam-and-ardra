from django.shortcuts import render, redirect
from core.models import Quiz, Card
from core.forms import QuizForm, CardForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "sign_in.html")

    else:
        quizzes = Quiz.objects.all().order_by('-date_created').prefetch_related('cards')

        return render(request, "index.html", {
            'quizzes': quizzes,  
        })

@login_required
def account(request):
    return render(request, "account.html")

@login_required
def quiz_detail(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    cards = quiz.cards.all()
    card_count = quiz.cards.count()

    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.quiz = quiz
            card.save()
            messages.success(request, f'Card "{card.answer}" Created')
            return redirect('quiz_detail', pk=quiz.pk)
        else:
            messages.warning(request, 'Sorry, something did not work. Make sure you fill out both question and answer fields.')

    else:
        form = CardForm()


    return render(request, 'quizzes/quiz_detail.html', {
        'quiz': quiz,
        'cards': cards,
        'form': form,
        'card_count': card_count,
    })


def sort_by_newest(request):
    quizzes = Quiz.objects.all().order_by('-date_created')
    return render(request, 'index.html', 
    {'quizzes': quizzes
    })

def sort_by_oldest(request):
    quizzes = Quiz.objects.all().order_by('date_created')
    return render(request, 'index.html', {
        'quizzes': quizzes
    })

@login_required
def delete_card(request, pk):
    """deletes a users card, user must be logged in"""
    
    card = Card.objects.get(pk=pk)
    quiz_id = card.quiz.id
    # if (request.user == quiz.author) or (request.user.is_staff):
    card.delete()
    messages.success(request, f'Card "{card}" Deleted')
    return redirect('quiz_detail', pk=quiz_id)
    # return render(request, 'quizzes/quiz_detail.html',)

@login_required
def delete_quiz(request, pk):
    """deletes a users quiz, user must be logged in"""
    # quiz = Quiz.objects.get(pk=pk)
    quiz = Quiz.objects.get(pk=pk)
    # if (request.user == quiz.author) or (request.user.is_staff):
    quiz.delete()
    messages.success(request, f'Quiz "{quiz}" Deleted')
    return redirect('home')
    # return render(request, 'quizzes/quiz_detail.html',)

@login_required
def play_quiz(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quiz_play.html', {
        'quiz': quiz,
    })

@login_required
def new_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.author = request.user
            quiz.save()
            messages.success(request, f'Quiz "{quiz}" Created')
            return redirect('home')
        # else:
        #     messages.warning(request, 'Sorry, something went wrong. Please try again!')
    else:
        form = QuizForm()

    return render(request, 'quizzes/new_quiz.html', {

        "form": form,
    })

@login_required
def edit_quiz(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    form_class = QuizForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=quiz)
        if form.is_valid():
            card = form.save(commit=False)
            card.save()
            messages.success(request, 'Select the plus sign below to add a card!')
            return redirect('quiz_detail', pk=quiz.pk)
        # else:
        #     messages.warning(request, 'Sorry, something did not work. Make sure you fill out both question and answer fields.')

            form.save()
            return redirect('home')
            # return redirect("quiz_detail", pk=quiz.pk)
    
    else:
        form = form_class(instance=quiz)
    return render(request, 'quizzes/edit_quiz.html', {'quiz': quiz, 'form': form, })

@login_required
def edit_card(request, pk):
    card = Card.objects.get(pk=pk)
    form_id = card.quiz.id
    form_class = CardForm
    
    if request.method =='POST':
        form = form_class(data=request.POST, instance=card)
        if form.is_valid():
            form.save()
            # return redirect('home')
            return redirect('quiz_detail', pk=form_id)

    else:
        form = form_class(instance=card)
    return render(request, 'cards/edit_card.html', {'card': card, 'form': form, })



