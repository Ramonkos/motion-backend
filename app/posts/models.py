from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):

    title = models.CharField(
        max_length=200
    )

    content_text = models.TextField(
        max_length=500
    )

    created = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True
    )

    updated = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True
    )

    author = models.ForeignKey(to=User, related_name='posts', on_delete=models.CASCADE)

    likes = models.ManyToManyField(to=User, related_name='likes', blank=True)

    def __str__(self):
        return f'Post {self.pk}: {self.title}'
