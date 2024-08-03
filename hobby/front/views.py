from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def main(request):
    temp = loader.get_template('home.html')
    return HttpResponse(temp.render())