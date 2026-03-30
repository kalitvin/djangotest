from django.contrib import admin

# Register your models here.

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ("title", "created_at", "is_published")
  list_filter = ("is_published", "created_at")
  search_fields = ("title", "body")