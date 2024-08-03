from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.main),
    path('quiz/', include('quiz.urls')),
]