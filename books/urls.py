from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^([0-9]+)/$', views.view, name="view"),
	url(r'^genre/([0-9]+)/$', views.by_genre, name="by_genre"), 
]