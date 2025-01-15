from django.shortcuts import render 
from django.views import generic
from .models import Post

# Create your views here.

# class based view that shows postlist
# It uses what's called a generic view, which allows us to quickly
# query the database pull all the information we ask for and send it
# to the template
class PostList(generic.ListView):
	# this gets all of our post objects in a var called queryset
	queryset = Post.objects.all()
	# this identifies our template to send all the post objects
	template_name = "blog/index.html"
	#we also create a paginate var
	paginate_by = 6
