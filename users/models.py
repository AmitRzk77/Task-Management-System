from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): #Used Abstract instead of models.Model because Abstact provides default authentication
                             # Supports password hashing & authentication | Has built-in fields 
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User')
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
   # email = models.CharField(max_length=)