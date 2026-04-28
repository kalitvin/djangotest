from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.templatetags.static import static
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="Пользователь",
    )
    avatar = models.ImageField(
        "Аватар",
        upload_to="avatars/",
        blank=True,
        null=True,
    )
    bio = models.TextField("О себе", blank=True)
    location = models.CharField("Город", max_length=100, blank=True)
    birth_date = models.DateField("Дата рождения", null=True, blank=True)
    
    @property
    def avatar_url(self):
        if self.avatar:
            try:
                return self.avatar.url
            except ValueError:
                # На случай, когда файл очищен, но объект ещё не пересохранён
                pass
        return settings.MEDIA_URL + 'avatars/default_avatar.png'

    def __str__(self):
      return f"Профиль пользователя {self.user.username}"
