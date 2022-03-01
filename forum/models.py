"""Imports"""
from django.db import models
from django.contrib.auth.models import User


#class Category(models.Model):
#    """Category model."""
#    category = models.CharField(max_length=30, unique=True, primary_key=True)


class Post(models.Model):
    """Post model."""
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forum_posts')
    content = models.TextField(blank=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
#    category = models.ForeignKey(Category, default='No Category', on_delete=models.SET_DEFAULT, related_name='post_category')
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    def __str__(self):
        return str(self.title)

    def likes_amount(self):
        return self.likes.count()
    
    class Meta:
        """Post Ordering"""
        ordering = ['-created_date', 'updated_date']


class Comments(models.Model):
    """Comments model."""
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name='post_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    body = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='comment_likes')

    def __str__(self):
        return f"Comment by {self.author}: {self.body}"

    class Meta:
        """Comment Ordering"""
        ordering = ['-created_date', 'updated_date']


