from django.shortcuts import render

# Create your views here.
def testimonials(request):
    context={'testimonials' : {
        'Alice': 'Outstanding work! Highly recommend.',
        'Bob': 'Professional and fast delivery.',
        'Charlie': 'Great communication and skills.'
    }}
    return render(request, 'testimonials/testimonials.html', context)