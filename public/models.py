import random
from string import ascii_letters, digits
from uuid import uuid4

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.db import models


class AccountManager(BaseUserManager):
    def create_user(self, first_name: str, last_name: str, email: str, password: str):
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=uuid4(),
            email=self.normalize_email(email),
        )
        salt = "".join(random.choices(ascii_letters + digits, k=random.randint(10, 20)))
        user.password_salt = salt
        user.password = make_password(password, salt=salt)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, first_name: str, last_name: str, email: str, password: str
    ):
        user = self.create_user(
            first_name=first_name, last_name=last_name, email=email, password=password
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.UUIDField(unique=True)
    avatar = models.ImageField(
        upload_to="account", default="account/user.jpeg", blank=True, null=True
    )
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)
    password_salt = models.CharField(max_length=20)
    date_joined = models.DateField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = AccountManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_superuser:
            return True
        return False

    def has_perms(self, perm, obj=None):
        if self.is_active and self.is_superuser:
            return True
        return False

    def has_module_perms(self, app_label):
        if self.is_active and self.is_superuser:
            return True
        return False
