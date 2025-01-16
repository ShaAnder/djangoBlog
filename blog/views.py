from django.shortcuts import render, get_object_or_404
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


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(request, "blog/post_detail.html", {"post": post},)
