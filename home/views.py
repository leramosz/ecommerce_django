from django.shortcuts import render
from books.models import Book
from authors.models import Author

# Create your views here.
def index(request):
	slider_books = Book.objects.filter(highlighted = True)
	new_books = Book.objects.filter(new = True)
	best_sellers = Book.objects.filter(best_seller = True)
	featured_authors = Author.objects.filter(featured = True)
	data = {'slider_books':slider_books, 'new_books':new_books, 
			'best_sellers':best_sellers, 'featured_authors': featured_authors}
	return render(request, 'home.html', data)
