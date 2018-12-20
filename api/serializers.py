from core.models import Quiz, Card, User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ('question', 'answer', 'right_answers', 'wrong_answers')

class QuizSerializer(serializers.HyperlinkedModelSerializer):
    cards = CardSerializer(many=True, required=False)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Quiz
        fields = ('url', 'owner', 'id', 'title', 'date_created', 'cards')

    def create(self, validated_data):
        cards_data = validated_data.pop('cards')
        quiz = Quiz.objects.create(**validated_data)
        for card_data in cards_data:
            Card.objects.create(quiz=quiz, **cards_data)
        return quiz