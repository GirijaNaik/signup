from django.db import models
from django.contrib.auth.models import AbstractUser

class UserManage(AbstractUser):
    username = models.CharField('username', max_length=20)
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('First name', max_length=20)
    last_name = models.CharField('Last name', max_length=20)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

def __str__(self):
    return f'{self.email} - {self.first_name} {self.last_name}'
