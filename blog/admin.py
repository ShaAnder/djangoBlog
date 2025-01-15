from django.contrib import admin
#import our post model here
from .models import Post, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)