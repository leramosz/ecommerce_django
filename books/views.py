from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'books.html')

def view(request, id):
	return render(request, 'book.html')

def by_genre(request, id):
	return render(request, 'books.html')