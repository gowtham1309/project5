from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_first(request):
    return HttpResponse('<marquee>this is app1 first project</marquee>')
def app1_second(request):
    return HttpResponse('<h1>this is app1 second project</h1>')