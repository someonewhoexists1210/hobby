from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.main, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('result/', views.result, name='result'),
]