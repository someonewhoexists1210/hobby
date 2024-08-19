from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .suggest import suggestHobby
from .models import Question, Response


# Create your views here.
def main(request):
    temp = loader.get_template('home.html')
    return HttpResponse(temp.render())

def quiz(request):
    questions = Question.objects.order_by('?')
    return render(request, 'quiz_home.html', {'questions': questions})

def result(request):
    if request.method == 'POST':
        question_ids = request.POST['question_ids'].split(',')
        answer_ids = []
        
        for question_id in question_ids:
            answer_ids.append(request.POST['question_' + question_id])
        for key, value in zip(question_ids, answer_ids):
            response = Response(question_id=key, answer_id=value, ip=request.META['REMOTE_ADDR'])
            response.save()
        suggested_hobbies = suggestHobby(answer_ids)
        return render(request, 'result.html', {'hobbies': suggested_hobbies})