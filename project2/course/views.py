from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Home Page</h1>')

def learn_django(request):
    return HttpResponse('<h1>Hello Django</h1>')

def learn_python(request):
    return HttpResponse('<h1>Hello Python</h1>')
    
def learn_flask(request):
    return HttpResponse('<h1>Hello Flask</h1>') 

def learn_math(request):
    a = 10 + 10
    return HttpResponse(f'Some of 10 + 10 is {a}.')

def learn_ml(request):
    return HttpResponse('<h1>Welcome to the world of Machine Learning</h1>')