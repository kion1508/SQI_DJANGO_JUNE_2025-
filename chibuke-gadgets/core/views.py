from django.shortcuts import render, HttpResponse

# Create your views here.
def greetings(request):
    return HttpResponse('<h2>How far now watin you wan buy</h2>')