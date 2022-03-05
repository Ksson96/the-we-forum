"""Imports"""
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required


def home_screen(request):
    """Home Screen View"""
    posts = Post.objects.all()
    context = {
        'posts': posts
        }
    return render(request, 'index.html', context)


def post(request, post_id):
    """Single Post View"""
    post = get_object_or_404(Post, post_id=post_id)
    comments = Comment.objects.filter(post=post)
    comment_form = CommentForm(request.POST)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == 'POST':
        if comment_form.is_valid():
            forum_post = comment_form.save(commit=False)
            forum_post.author = request.user
            forum_post.post = post
            forum_post.save()
            return redirect(request.path_info)

    context = {
        'post': post,
        'comments': comments,
        'liked': liked,
        'comment_form': comment_form
    }
    return render(request, 'post.html', context)


def edit_post(request, post_id):
    """Edit Post View"""
    post = get_object_or_404(Post, post_id=post_id)
    if request.user == post.author:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                updated_post = form.save(commit=False)
                updated_post.author = request.user
                updated_post.save()
                return redirect('home')

        form = PostForm(instance=post)
        context = {
            'form': form
        }
        return render(request, 'edit_post.html', context)


@login_required()
def create_post(request):
    """Create Post View"""
    form = PostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('home')

    context = {'form': form}
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


@login_required()
def like_post(request, post_id):
    """Like Post View"""
    post = get_object_or_404(Post, post_id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

