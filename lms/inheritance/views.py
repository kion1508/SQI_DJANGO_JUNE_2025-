from django.shortcuts import render

# Create your views here.
def demo_inheritance(request):
    context={'how_i_feel':'i am tired'}
    return render(request,'inheritance/inheritance.html',context)