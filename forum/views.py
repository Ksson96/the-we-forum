from django.shortcuts import render

# Create your views here.

def home_screen(request):
    print(request)
    return render(request, "index.html", {})


def create_post(request):
    print(request)
    return render(request, "create_post.html", {})