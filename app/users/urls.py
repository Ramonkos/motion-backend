from django.urls import path
from users.views import ListUsers, ListUser, ToggleFollow, ListFollowers, ListFollowing

urlpatterns = [
    path('', ListUsers.as_view()),
    path('<int:pk>/', ListUser.as_view()),
    path('followers/toggle-follow/<int:pk>/', ToggleFollow.as_view()),
    path('followers/following/', ListFollowing.as_view()),
    path('followers/followers/', ListFollowers.as_view()),
]