from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def caption(request):
    return HttpResponse('<h1>Ruturaj is caption of csk</h1>')
