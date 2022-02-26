from django import forms
from allauth.account.forms import LoginForm
from .models import Post



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


# class CustomLoginForm(LoginForm):
#     def __init__(self, *args, **kwargs):
#         super(CustomLoginForm(), self).__init__(*args, **kwargs)
#         self.fields['login'].widget = forms.TextInput(attrs={'type': 'email', 'class': 'yourclass'})
#         self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'yourclass'})
#         return




# class CustomLoginForm(LoginForm):
#     fields = ('username', 'password')
#     widgets = {
#         'username': forms.TextInput(attrs={'class': 'form-control'}),
#         'password': forms.PasswordInput(attrs={'class': 'form-control'})
#         }