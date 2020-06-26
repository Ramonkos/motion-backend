from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response

from permissions.models import IsOwnerOrReadOnly
from posts.models import Post
from posts.serializers import CreateListPostsSerializer


class CreateListPosts(GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = CreateListPostsSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(serializer.data)


class ListUpdateDeletePost(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = CreateListPostsSerializer


class ListLikedPosts(ListAPIView):
    # queryset = Post.objects.all()
    serializer_class = CreateListPostsSerializer

    # def get(self, request, *args, **kwargs):
    #     queryset = self.get_queryset().filter(likes=request.user)
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    def get_queryset(self):
        return self.request.user.likes


class ListFromFollowingPosts(ListAPIView):
    # serializer_class = CreateListPostsSerializer
    #
    # def get_queryset(self):
    #     return self.request.user.likes
    pass


class ToggleLikePosts(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CreateListPostsSerializer

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user

        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)
        return Response(self.get_serializer(post).data)
