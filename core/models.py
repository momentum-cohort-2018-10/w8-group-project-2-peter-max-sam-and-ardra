from django.db import models
from django.contrib.auth.models import User




class Quiz(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quizzes")
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.title


class Card(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="cards")
    question = models.TextField(blank=False, null=False)
    answer = models.TextField(blank=False, null=False)
    right_answers = models.IntegerField(default="0")
    wrong_answers = models.IntegerField(default="0")



    # pref one id per url if possible 
    # every answer has its own unique id 
    # Delete /answers/2 rather than Delete /post/1/answers/2