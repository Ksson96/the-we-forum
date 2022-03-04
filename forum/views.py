"""Imports"""
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.models import User


def home_screen(request):
    """Home Screen View"""
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'index.html', context)


def post(request, post_id):
    """Single Post View"""
    post = get_object_or_404(Post, post_id=post_id)
    comments = Comment.objects.filter(post=post)
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
    if request.user == post.author:
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


def delete_post(request, post_id):
    """Delete Post"""
    post = get_object_or_404(Post, post_id=post_id)
    if request.user == post.author:
        post.delete()
    
    return redirect('home')


def delete_comment(request, comment_id):
    """Delete Comment"""
    comment = get_object_or_404(Comment, comment_id=comment_id)
    if request.user == comment.author:
        comment.delete()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def like_post(request, post_id):
    """Like Post View"""
    post = get_object_or_404(Post, post_id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)       
    else:
        post.likes.add(request.user)
        
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

