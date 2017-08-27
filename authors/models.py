from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=100)
	biography = models.TextField()
	image = models.CharField(max_length=100)
	featured = models.BooleanField()