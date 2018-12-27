from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
from .models import Quiz, Card
import json
# from initialdata.quizzes import 


def get_path(file):
    return os.path.join(settings.BASE_DIR, 'initial_data', file)

class Command(BaseCommand):
    help = "generate quizzes"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        print("Deleting quizzes")
        Quiz.objects.all().delete()
        with open(get_path('quizzes.json'), 'r') as file:
            reader = json.DictReader(file)
            i = 0
            for row in reader:
                i += 1
                quiz = Quiz(
                    author=
                )
