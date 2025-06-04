from django.shortcuts import render
def welcome(request):
    return render(request,'my_app/my_app.html')
# Create your views here.
