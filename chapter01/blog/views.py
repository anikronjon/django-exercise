from django.shortcuts import render
from django.views import generic
from .models import Category, Post, Media


# List Of Post
class PostsView(generic.ListView):
    """List of post view"""
    queryset = Post.publish_objects.all()