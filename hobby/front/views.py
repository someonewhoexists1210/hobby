from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Question, Answer


# Create your views here.
def main(request):
    temp = loader.get_template('home.html')
    return HttpResponse(temp.render())

def quiz(request):
    questions = Question.objects.all()
    return render(request, 'quiz_home.html', {'questions': questions})

def result(request):
    if request.method == 'POST':
        id = request.POST['question_id']
        answer = Answer.objects.get(id=request.POST['question_' + id])
        
        print(str(Question.objects.get(id=id)))
        print(str(answer))
        return(HttpResponse('Thanks for submitting your answers!'))