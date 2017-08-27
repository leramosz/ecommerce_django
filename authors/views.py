from django.shortcuts import render
from .models import Author
from genre.models import Genre
from books.models import Book

def index(request):
	genres = Genre.objects.all()
	authors = Author.objects.all()
	grid = len(authors) > 3
	data = {'authors':authors, 'genres':genres, 'grid':grid}
	return render(request, 'authors.html', data)

def view(request, id):
	try:
		author = Author.objects.get(id = id)
	except Exception:
		data = {'page': {'view': 'index_authors', 'name': 'Authors'}}
		return render(request, 'error.html', data)
	author_books = Book.objects.filter(author__id = author.id)
	grid = len(author_books) >= 4
	data = {'author':author, 'author_books':author_books, 'grid':grid}
	return render(request, 'author.html', data)

def by_genre(request, id):
	try:
		selected_genre = Genre.objects.get(id = id)
	except Exception:
		data = {'page': {'view': 'index_authors', 'name': 'Authors'}}
		return render(request, 'error.html', data)
	genres = Genre.objects.all()
	authors = Author.objects.all()
	grid = len(authors) > 3
	data = {'authors':authors, 'genres':genres, 'selected_genre': selected_genre, 'grid': grid}
	return render(request, 'authors.html', data)
