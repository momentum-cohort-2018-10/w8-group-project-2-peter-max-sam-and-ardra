from rest_framework import serializers
from core.models import Quiz, Card, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)

class CardSerializer(serializer.ModelSerializer):
    class Meta:
        model = Card
        fields = ("id", "question", "answer", "quiz", "right_answers", "wrong_answers",)

class QuizSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, required=False)
    owner = serializers.SlugRelatedField(slug_field="username", read_only=True)
    



# class Quiz(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quizzes")
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True, max_length=255)
#     date_created = models.DateField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = "Quizzes"

#     def __str__(self):
#         return self.title