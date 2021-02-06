from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=300)
    img = models.CharField(max_length=100)
    userRecipe = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
