from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.conf import settings
# Create your models here.
class CustomUser(AbstractUser):
    
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    #image = models.ImageField(blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='user_profile')

    def __str__(self):
        return self.user.email

