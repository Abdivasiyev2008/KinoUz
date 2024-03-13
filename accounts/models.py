from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    
    def __str__(self):
        return str(self.username)
