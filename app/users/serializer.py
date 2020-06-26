from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class ListUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['avatar', 'first_name', 'last_name', 'location', 'about_me', 'things_user_likes']

