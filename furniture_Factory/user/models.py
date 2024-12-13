from django.db import models
from django.contrib.auth.models import AbstractUser


class User():
    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('supervisor', 'Начальник цеха'),
        ('worker', 'Рабочий'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='worker')
    full_name = models.CharField(max_length=255)