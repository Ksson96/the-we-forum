from django import forms
from allauth.account.forms import LoginForm
from .models import Post, Comments



class PostForm(forms.ModelForm):
    class Meta:
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
    class Meta:
        model = Comments
        fields = ('body',)
        labels = {
            'body': ('Leave a comment:'),
        }
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 6 })
        }