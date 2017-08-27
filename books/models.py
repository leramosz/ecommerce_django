from django.db import models
from authors.models import Author

class Book(models.Model):
	author = models.ForeignKey(Author)
	name = models.CharField(max_length=100)
	overview = models.TextField()
	price = models.FloatField()
	sale_off = models.FloatField(default=0)
	image = models.CharField(max_length=100)
	rating = models.IntegerField()
	hot = models.BooleanField()
	highlighted = models.BooleanField()
	new = models.BooleanField()
	best_seller = models.BooleanField()