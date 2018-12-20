from django.contrib import admin
from core.models import Quiz, Card


class CardsInLine(admin.StackedInline):
    model = Card
    list_display = ("quiz", "question", "answer",)


class QuizAdmin(admin.ModelAdmin):
    model = Quiz
    list_display = ("title", "author", "date_created")
    inlines = [CardsInLine]


admin.site.register(Quiz, QuizAdmin)