from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class CustomUserManager(UserManager):
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    objects = CustomUserManager()

    username = None
    email = models.EmailField(verbose_name='Почта', unique=True)
    telephone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватарка', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
