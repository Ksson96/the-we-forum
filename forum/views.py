"""Imports"""
from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.contrib.auth.models import User


def home_screen(request):
    """Home Screen View"""
    print(request.headers)
    posts = Post.objects.all()
    print(User)
    context = {'posts':posts}
    return render(request, 'index.html', context)


def create_post(request):
    """Create Post View"""
    form = PostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
        else:
            print("ERROR : Form is invalid")
            print(form.errors)

    context = {'form':form}
    return render(request, 'create_post.html', context)