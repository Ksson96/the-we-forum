"""Imports"""
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, CommentForm
from .models import Post, Comments
from django.contrib.auth.models import User


def home_screen(request):
    """Home Screen View"""
    print(request.headers)
    posts = Post.objects.all()
    print(User)
    context = {'posts':posts}
    return render(request, 'index.html', context)


def post(request, post_id):
    """Single Post View"""
    post = get_object_or_404(Post, post_id=post_id)
    comments = Comments.objects.filter(post=post)
    comment_form = CommentForm(request.POST)
    if request.method == 'POST':
        if comment_form.is_valid():
            obj = comment_form.save(commit=False)
            obj.author = request.user
            obj.post = post
            obj.save()
            return redirect(request.path_info)
        else:
            print("ERROR : Form is invalid")
            print(comment_form.errors)

    context = {
        'post':post,
        'comments':comments,
        'comment_form':comment_form
    }
    return render(request, 'post.html', context)


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
    form = PostForm(request.POST)
    if request.method == 'POST':
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




