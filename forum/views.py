"""Imports"""
from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.contrib.auth.models import User


def home_screen(request):
    """Home Screen View"""
    print(request.headers)
    return render(request, 'index.html', {})


def create_post(request):
    """Create Post View"""
    form = PostForm(request.POST)
    if request.method == 'POST':
        print('Printing post:', request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            print('Printing date:', obj.created_date, obj.content)
        else:
            print("ERROR : Form is invalid")
            print(form.errors)

    context = {'form':form}
    return render(request, 'create_post.html', context)