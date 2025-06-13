from django.shortcuts import render

# Create your views here.
def services(request):
    services_list = ["Web Development", "UI/UX Design", "SEO Optimization", "Content Writing"]
    return render(request, 'portfolio/services.html', {'services': services_list})


def testimonials(request):
    testimonials = {
        'Alice': 'Outstanding work! Highly recommend.',
        'Bob': 'Professional and fast delivery.',
        'Charlie': 'Great communication and skills.'
    }
    return render(request, 'portfolio/testimonials.html', {'testimonials': testimonials})

def pricing(request):
    pricing = {
        'Web Development': '$1000',
        'Graphic Design': '$500',
        'SEO Optimization': '$600'
    }
    return render(request, 'portfolio/pricing.html', {'pricing': pricing})


def blog(request):
    return render(request, 'portfolio/blog.html')


def home(request):
    return render(request, 'portfolio/home.html')

def case_studies(request):
    return render(request, 'portfolio/case_studies.html')