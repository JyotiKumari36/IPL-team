from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def caption(request):
    return HttpResponse('<h1><marquee direction=right>king kohli is caption of csk</marquee></h1>')

