from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'quizzes', views.QuizViewSet)
router.register(r'cards', views.CardViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
]