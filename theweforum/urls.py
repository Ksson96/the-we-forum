"""theweforum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.edit import CreateView
from forum import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_screen, name="home"),
    path('accounts/', include('allauth.urls')),
    path('create_post', views.create_post, name="create_post"),
    path('edit_post/<post_id>', views.edit_post, name="edit_post"),
    path('post/<int:post_id>', views.post, name="post"),
    path('delete_post/<int:post_id>', views.delete_post, name="delete_post"),
    path('delete_comment/<comment_id>', views.delete_comment, name="delete_comment"),
    path('like_post/<post_id>', views.like_post, name="like_post"),
    path('accounts/signup', CreateView.as_view(success_url='home')),
]
