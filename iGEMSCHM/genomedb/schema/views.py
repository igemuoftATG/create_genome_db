from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, welcome to the GenomeDB Database, have a good day!")

