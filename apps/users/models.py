#!/env/bin/python3
"""
------------------------------
Define CustomUserModel class
------------------------------
"""
import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# My models
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    ----------------------------------
    Custom User Model with email field
    ----------------------------------
    """

    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(verbose_name=_("Username"), max_length=255, unique=True)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=50)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=50)
    email = models.EmailField(verbose_name=_("Email"), max_length=255, unique=True)
    is_active = models.BooleanField(verbose_name=_("Is Active"), default=True)
    is_staff = models.BooleanField(verbose_name=_("Is Staff"), default=False)
    date_joined = models.DateTimeField(
        verbose_name=_("Date Joined"), default=timezone.now
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-date_joined"]

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        """
        ------------------------------
        Return the user's full name
        ------------------------------
        """
        return f"{self.first_name} {self.last_name}"

    @property
    def get_short_name(self):
        """
        ------------------------------
        Return the user's short name
        ------------------------------
        """
        return self.username
