from django.shortcuts import render

# Create your views here.
def available_dishes(request):
    context={'name':'garri',
             'price':50
             }
    return render(request,'menu/dishes.html',context)