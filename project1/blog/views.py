from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Comment
from .forms import *



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
    query = request.GET.get("q", "").strip()
    posts_qs = Post.objects.filter(is_published=True)
    if query:
        posts_qs = posts_qs.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )

    # пагинация
    paginator = Paginator(posts_qs, 2)  # 5 постов на страницу
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "posts": page_obj,   # теперь posts = текущая страница
        "page_obj": page_obj,
        "query": query,
    }


    # posts = Post.objects.filter(is_published=True).order_by("-created_at")
    # context = {"posts": posts}
    return render(request, "blog/post_list.html", context)

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_published=True)
    comments = post.comments.all().order_by("-created_at")

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = CommentForm()

    context = {"post": post, "comments": comments, "form": form}
    return render(request, "blog/post_detail.html", context)

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)

    context = {"form": form, "post": post}
    return render(request, "blog/post_form_edit.html", context)

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("post_list")

    context = {"post": post}
    return render(request, "blog/post_confirm_delete.html", context)

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("post_list")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})