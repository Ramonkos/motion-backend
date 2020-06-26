from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    # Field used for authentication
    USERNAME_FIELD = 'email'

    # Additional fields required when using createsuperuser (USERNAME_FIELD and passwords are always required)
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(unique=True)

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    avatar = models.ImageField()

    banner = models.ImageField()

    location = models.CharField(
        max_length=100
    )

    about_me = models.TextField(
        max_length=500
    )

    things_user_likes = models.TextField(
        max_length=500
    )

    created = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True
    )

    following = models.ManyToManyField(
        #to=settings.AUTH_USER_MODEL,
        to='self',
        symmetrical=False,
        blank=True,
        related_name='followers'
    )

    def __str__(self):
        return self.username
