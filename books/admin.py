from django.contrib import admin
from .models import	Book

class BookAdmin(admin.ModelAdmin):
	model = Book
	list_display = ['id', 'author_id', 'name', 'overview', 'price', 'sale_off', 
					'rating', 'image', 'hot', 'highlighted', 'new', 'best_seller']

	def author_id(self, obj):
		return obj.author.id

admin.site.register(Book, BookAdmin)