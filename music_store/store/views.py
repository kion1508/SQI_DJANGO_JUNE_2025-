from django.shortcuts import render
from .models import Artist, Album, Song
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
def song(request):
    
    context={
        'songs': Song.objects.select_related('album').all(),
        'song_artists':Song.objects.get(),
        
    }

    return render (request,'store/song.html',context)