from django.db import models
from django.contrib.auth.Model import User



class Post(models.Model):

    post_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forum_posts')
    content = models.TextField(blank=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, related_name='post_category')
    likes = models.ManyToManyField(User, related_name='post_likes')


class Comments(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_comments')
    body = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='comment_likes')
