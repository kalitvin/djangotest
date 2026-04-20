"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from blog import views

from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"), # главная страница
    path("about/", views.about , name="about"), # О проекте
    path("post_list/", views.post_list , name="post_list"), # Список постов
    path("blog/<int:pk>/", views.post_detail, name="post_detail"), # Детализация поста
    path("blog/create/", views.post_create, name="post_create"),
    path("blog/<int:pk>/edit/", views.post_edit, name="post_edit"),
    path("blog/<int:pk>/delete/", views.post_delete, name="post_delete"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
]
