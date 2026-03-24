from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#def home(request):
#    return HttpResponse("<h1>Главная страница</h1><p>Добро пожаловать!</p>")
def home(request):
    return render(request, "blog/home.html")

def about(request):
    return HttpResponse("<h1>О проекте</h1><p>Учебный блог на Django.</p>")

def post_list(request):
    return HttpResponse("<h1>Блог</h1><p>Здесь будет список постов.</p>")
