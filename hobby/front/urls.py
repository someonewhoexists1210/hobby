from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('result/', views.result, name='result'),
    path('read/', views.read, name='read'),
    path('write/', views.write, name='write'),
]