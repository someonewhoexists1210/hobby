from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('result/', views.result, name='result'),
    path('page/<str:hobby>', views.read, name='read'),
]