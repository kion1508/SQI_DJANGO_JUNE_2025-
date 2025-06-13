from django.shortcuts import render

# Create your views here.
def case_studies(request):
    return render(request, 'case_studies/case_studies.html')