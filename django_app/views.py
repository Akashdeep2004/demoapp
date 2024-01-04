from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def application(request):
    return HttpResponse("Hello world!")