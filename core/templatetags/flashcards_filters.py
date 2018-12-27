from django import template 

register = template.Library()

@register.filter(name='card_count')
def card_count(quiz):
    cards = quiz.cards.all().count()
    return cards 