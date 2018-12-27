from core.models import Quiz, Card, User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'url', 'question', 'answer', 'right_answers', 'wrong_answers')

class QuizSerializer(serializers.HyperlinkedModelSerializer):
    cards = CardSerializer(many=True, required=False)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Quiz
        fields = ('url', 'author', 'id', 'title', 'date_created', 'cards')


