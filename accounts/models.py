from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import Usermanager
# Create your models here.

class CustomUser(AbstractUser):
    username = None
    phone_num = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50)
    user_img = models.ImageField(upload_to="profile")

    USERNAME_FIELD = 'phone_num'
    REQUIRED_FIELDS = []
    objects = Usermanager()

    def __str__(self):
        return self.email