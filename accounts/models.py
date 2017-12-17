from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from .managers import UserManager

USERNAME_REGEX = '^[a-z0-9._-]*$'


class User(AbstractUser):
    first_name = None
    last_name = None

    username = models.CharField(
        max_length=256,
        unique=True,
        blank=False,
        validators=[
            RegexValidator(
                regex=USERNAME_REGEX,
                message='Username must contain: a-z, 0-9 or ".-_" ',
                code='invalid_username'
                )
            ]
        )

    email = models.EmailField(unique=True, blank=False)

    USERNAME_FIELD = 'email'  # use email to log in
    REQUIRED_FIELDS = ['username']  # required when user is created

    objects = UserManager()

    def __str__(self):
        return self.username
