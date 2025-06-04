from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('welcome to the home page!!!!')