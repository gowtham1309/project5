from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_first(request):
    return HttpResponse('<marquee>this is app2 first project</marquee>')
def app2_second(request):
    return HttpResponse('<h1>this is app2 second project</h1>')
