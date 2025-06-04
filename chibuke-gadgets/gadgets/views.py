from django.shortcuts import render, HttpResponse

# Create your views here.
def gadgets(request):
    return HttpResponse("""
        <ol>
            <li>printer</li>
            <li>television</li>
            <li>laptop</li>
            <li>fan</li>
        </ol>'
       """ )