from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def projects(requests):
    return HttpResponse("hello")