from django.shortcuts import render
from .models import Book
from genre.models import Genre

# Create your views here.
def index(request):
	genres = Genre.objects.all()
	books = Book.objects.all()
	grid = len(books) > 3
	data = {'books':books, 'genres':genres, 'grid':grid}
	return render(request, 'books.html', data)

def view(request, id):
	try:
		book = Book.objects.get(id = id)
	except Exception:
		data = {'page': {'view': 'index_books', 'name': 'Books'}}
		return render(request, 'error.html', data)
	data = {'book':book}
	return render(request, 'book.html', data)

def by_genre(request, id):
	try:
		selected_genre = Genre.objects.get(id = id)
	except Exception:
		data = {'page': {'view': 'index_books', 'name': 'Books'}}
		return render(request, 'error.html', data)
	genres = Genre.objects.all()
	books = Book.objects.all()
	grid = len(books) > 3
	data = {'books':books, 'genres':genres, 'selected_genre': selected_genre, 'grid': grid}
	return render(request, 'books.html', data)