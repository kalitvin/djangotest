from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

#def home(request):
#    return HttpResponse("<h1>Главная страница</h1><p>Добро пожаловать!</p>")
def home(request):
    return render(request, "blog/home.html")

def about(request):
    return render(request, "blog/about.html")

# def post_list(request):
#   return render(request, "blog/post_list.html")

def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by("-created_at")
    context = {"posts": posts}
    return render(request, "blog/post_list.html", context)
