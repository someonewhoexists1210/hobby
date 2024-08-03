from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Question, Responses


# Create your views here.
def main(request):
    temp = loader.get_template('home.html')
    return HttpResponse(temp.render())

def quiz(request):
    questions = Question.objects.order_by('?')[:3]
    return render(request, 'quiz_home.html', {'questions': questions})

def result(request):
    if request.method == 'POST':
        question_ids = request.POST['question_ids'].split(',')
        answer_ids = []
        for question_id in question_ids:
            answer_ids.append(request.POST['question_' + question_id])
        results = dict(zip(question_ids, answer_ids)) 
        for key, value in results.items():
            response = Responses(question_id=key, answer_id=value, ip=request.META['REMOTE_ADDR'])
            response.save()
        return(HttpResponse('Thank you for taking the quiz!'))