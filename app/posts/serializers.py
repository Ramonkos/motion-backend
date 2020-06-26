from rest_framework import serializers

from users.serializer import ListUsersSerializer
from .models import Post


class CreateListPostsSerializer(serializers.ModelSerializer):
    author = ListUsersSerializer(write_only=False)

    class Meta:
        model = Post
        fields = ['title', 'content_text', 'likes', 'created', 'author']
        depth = 2


