from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first_response(request):
    return HttpResponse('This is my first response')
def second_response(request):
    return HttpResponse('This is my second response')
def third_response(request):
    return HttpResponse('This is third response')
