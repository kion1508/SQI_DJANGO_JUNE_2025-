from django.shortcuts import render

# Create your views here.
def services(request):
    services= {'services' : ['Web Development', 'Graphic Design', 'SEO Optimization', 'Consulting']}
    return render(request, 'services/services.html', context=services)