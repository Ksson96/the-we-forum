from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """Create A Post"""
    class Meta:
        """Meta Class"""
        model = Post
        fields = ('title', 'content')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
                }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'optional'})
        }


class CommentForm(forms.ModelForm):
    """Post A Comment"""
    class Meta:
        """Meta Class"""
        model = Comment
        fields = ('body',)
        labels = {
            'body': ('Leave a comment:'),
        }
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }