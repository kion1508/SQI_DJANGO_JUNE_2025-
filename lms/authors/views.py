from django.shortcuts import render
from .models import Author
from library.models import Book

# Create your views here.


def all_authors(request):
    return render(request,'authors/authors.html')

def book_signings(request):
    return render(request,'authors/book-signings.html')
def mvt(request):

    authors = Author.objects.all()
    authors_ordered_by_birthdate = Author.objects.order_by('birth_date')
    books_ordered_by_title = Book.objects.order_by('-title')
    context = {
        'authors': authors,
        'authors_ordered_by_birthdate': authors_ordered_by_birthdate,
        'books_ordered_by_title': books_ordered_by_title,
    }
    return render(request,'authors/mvt.html',context)