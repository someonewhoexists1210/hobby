from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('result/', views.result, name='result'),
    path('pages/<str:hobby>', views.findpage, name='findpage'),
    path('pages/', views.page_page, name='pages'),
    path('create/', views.create_question, name='create'),
]