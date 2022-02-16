"""Imports"""
from django.shortcuts import render
from .forms import PostForm


def home_screen(request):
    """Home Screen View"""
    print(request.headers)
    return render(request, 'index.html', {})


def create_post(request):
    """Create Post View"""
    form = PostForm()
    if request.method == 'POST':
        print('Printing post:', request.POST)

    context = {'form':form}
    return render(request, 'create_post.html', context)