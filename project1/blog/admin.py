from django.contrib import admin

# Register your models here.

from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ("title", "created_at", "is_published")
  list_filter = ("is_published", "created_at")
  search_fields = ("title", "body")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "created_at")
    list_filter = ("created_at",)
    search_fields = ("author", "text")
