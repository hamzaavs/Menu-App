from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Bu alan zorunludur")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    roles = models.ManyToManyField('Role', blank=True)

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'phone']

    objects = UserManager()

    def __str__(self):
        return self.name


