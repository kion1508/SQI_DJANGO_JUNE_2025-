from django.shortcuts import render

# Create your views here.
def pricing(request):
    context={'pricing' : {
        'Web Development': '$1000',
        'Graphic Design': '$500',
        'SEO Optimization': '$600'
    }}
    return render(request, 'pricing/pricing.html',context)