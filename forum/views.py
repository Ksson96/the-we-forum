"""Imports"""
from django.shortcuts import render, get_object_or_404, redirect
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


def edit_post(request, post_id):
    """Edit Post View"""
    post = get_object_or_404(Post, post_id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('home')
        else:
            print("ERROR : Form is invalid")
            print(form.errors)

    form = PostForm(instance=post)
    context = {
        'form':form
    }
    return render(request, 'edit_post.html', context)


def create_post(request):
    """Create Post View"""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('home')
        else:
            print("ERROR : Form is invalid")
            print(form.errors)

    context = {'form':form}
    return render(request, 'create_post.html', context)