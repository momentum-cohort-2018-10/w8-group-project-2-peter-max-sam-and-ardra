"""flashcards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', views.index, name="home"),
    path('quiz/<int:pk>/', views.quiz_detail, name='quiz_detail'),
    # path('quiz/<int:pk>/', views.new_card, name='new_card'),
    path('quiz/new/', views.new_quiz, name='new_quiz'),
    # path('quiz/<int:pk>/new/card', views.new_card, name='new_card'),
    path('quiz/<int:pk>/edit/', views.edit_quiz, name='edit_quiz'),
    path('quiz/<int:pk>/edit/card', views.edit_card, name='edit_card'),
    path('quiz/<int:pk>/delete', views.delete_card, name='delete_card'),
    path('quiz/<int:pk>/delete_quiz', views.delete_quiz, name='delete_quiz'),
    # path('quiz/<int:pk>/take_quiz', views.take_quiz, name='take_quiz'),
    # path('quiz/<int:pk>/new/card', views.new_card, name='new_card'),
    path('quiz/<int:pk>/playquiz/', views.play_quiz, name="play_quiz"),
    path('quiz/newest/', views.sort_by_newest, name='sort_by_newest'),
    path('quiz/oldest/', views.sort_by_oldest, name='sort_by_oldest'),
]
