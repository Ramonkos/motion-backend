from django.urls import path
from posts.views import CreateListPosts, ListUpdateDeletePost, ListLikedPosts, ToggleLikePosts, ListFromFollowingPosts

urlpatterns = [
    path('', CreateListPosts.as_view()),
    path('<int:pk>/', ListUpdateDeletePost.as_view()),
    path('likes/', ListLikedPosts.as_view()),
    path('following/', ListFromFollowingPosts.as_view()),
    path('toggle-like/<int:pk>/', ToggleLikePosts.as_view()),
]
