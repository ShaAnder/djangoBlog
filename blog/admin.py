from django.contrib import admin
#import our post model here
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# we want to create an admin class, this is for the summernote upgrade
# everything added in here will upgrade the admin panel for superuser
# functionality the decorator allows us to register it as the post model
# so we don't need to create a model register for it.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Comment)