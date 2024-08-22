from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from.forms import CreationForm
from .suggest import suggestHobby, all_hobbies
from .models import Question, Answer, Response


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
    
def findpage(request, hobby):
    return render(request, f'hobbies/{hobby}.html')

def page_page(request):
    return render(request, 'page_home.html', {'hobbies': all_hobbies()})

def create_question(request):
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            question_text = form.cleaned_data['question']
            answers = [form.cleaned_data[f'answer{i}'] for i in range(1, 5)]
            
            question = Question.objects.create(text=question_text)
            for answer_text in answers:
                Answer.objects.create(question=question, text=answer_text)
            
            return redirect('home')
    else:
        form = CreationForm()
    
    return render(request, 'createQ.html', {'form': form})
