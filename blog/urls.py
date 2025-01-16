from . import views 
from django.urls import path

urlpatterns = [
	path('', views.PostList.as_view(), name='home'),
    #add a path to our post detail using the slug to identify which posts
	path('<slug:slug>/', views.post_detail, name='post_detail'),
]
