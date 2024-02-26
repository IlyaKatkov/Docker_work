from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=50, verbose_name='имя')
    email = models.EmailField(unique=True, verbose_name='email')
    phone_number = models.CharField(max_length=50, verbose_name='номер телефона')
    city = models.CharField(max_length=100, verbose_name='город')
    avatar = models.ImageField(upload_to='users', **NULLABLE, verbose_name='аватар')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'