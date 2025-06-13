from django.shortcuts import render
from .models import Artist, Album
# Create your views here.
def artist(request):
    
    artists=Artist.objects.order_by('debut_year')
    context= {'artists':artists}
    
    return render(request,'store/artist.html',context)

def album(request):
    context={
        'albums':Album.objects.select_related('artist').all().order_by('release_date')
    }
    return render (request,'store/album.html',context)
def home(request):
    return render (request,'store/home.html')