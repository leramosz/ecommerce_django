from django.contrib import admin
from .models import	Author

class AuthorAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'biography', 'image', 'featured']

admin.site.register(Author, AuthorAdmin)