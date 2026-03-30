from django.db import models

# Create your models here.

class Post(models.Model):
  title = models.CharField("Заголовок", max_length=200)
  body = models.TextField("Текст")
  created_at = models.DateTimeField("Создано", auto_now_add=True)
  updated_at = models.DateTimeField("Обновлено", auto_now=True)
  is_published = models.BooleanField("Опубликовано", default=True)
  def __str__(self):
    return self.title