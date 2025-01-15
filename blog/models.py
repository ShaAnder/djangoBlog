from django.db import models
#import our model class here
from django.contrib.auth.models import User

# our status const, this is to track published or draft statuses
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

# our post model here takes the argument of the the model class
class Post(models.Model):
	# title with a characterfield of 200 chars, is unique
	title = models.CharField(max_length=200, unique=True)
	# slugfield is a charfield but allows numbers, hypens ect
	slug = models.SlugField(max_length=200, unique=True)
	# author field, gives us the user data, cascade option and related table
	# this is our foreign key back to the user
	author = models.ForeignKey(
		User, 
		on_delete=models.CASCADE, 
		related_name="blog_posts" 
	)
	# a text field for the comment body
	content = models.TextField()
	excript = models.TextField(blank=True)
	# date time field to show when created
	created_on = models.DateTimeField(auto_now_add=True)
	# and our status for the post, whether it's a draft or published
	status = models.IntegerField(choices=STATUS, default=0)

class Comment(models.Model):
	post = models.ForeignKey(
		Post, 
		on_delete=models.CASCADE, 
		related_name="comments" 
	)
	author = models.ForeignKey(
		User, 
		on_delete=models.CASCADE, 
		related_name="commenter" 
	)
	body = models.TextField()
	approved = models.BooleanField(default=False)
	created_on = models.DateTimeField(auto_now_add=True)
