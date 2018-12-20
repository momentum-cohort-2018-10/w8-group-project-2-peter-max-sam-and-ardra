from rest_framework import serializers
from core.models import Quiz, Card, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ("quiz", "id", "question", "answer", "right_answers", "wrong_answers",)

class QuizSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, required=False)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Quiz
        fields = ("id", "owner", "title", "date_created", "cards",)

    def create(self, validated_data):
        cards_data = validated_data.pop('cards')
        quiz = Quiz.objects.create(**validated_data)
        for card_data in cards_data:
            Card.objects.create(quiz=quiz, **cards_data)
        return quiz

    
        # extra_kwargs = {
        #     'url': {'view_name': 'quiz', 'lookup_field': 'title'},
        # }

