from django import forms
from .models import Quiz, Card

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('title',)

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('question', 'answer',)


