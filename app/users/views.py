from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from users.serializer import ListUsersSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class ListUsers(ListAPIView):
    queryset = User.objects.all()
    serializer_class = ListUsersSerializer


class ListUser(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ListUsersSerializer


class ToggleFollow(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ListUsersSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        user_to_follow = self.get_object()

        if user_to_follow in user.following.all():
            user.following.remove(user_to_follow)
        else:
            user.following.add(user_to_follow)
        return Response(self.get_serializer(user).data)


class ListFollowers(ListAPIView):
    queryset = User.objects.all()
    serializer_class = ListUsersSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        follower_list = User.objects.all().filter()




class ListFollowing(ListAPIView):
    queryset = User.objects.all()
    serializer_class = ListUsersSerializer

    def get_queryset(self):
        return self.request.user.following.all()

    # def get(self, request, *args, **kwargs):
    #     user = request.user
    #     user_is_following = user.following.all()
    #     serializer = self.get_serializer(user_is_following)
    #     return Response(serializer.data)