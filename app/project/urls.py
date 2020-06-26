from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('backend/api/users/', include('users.urls')),
    path('backend/api/social/posts/', include('posts.urls')),
    path('backend/api/social/', include('users.urls')),

    # token
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_refresh'),

    # api/docs
    path('api/docs/', include_docs_urls(title='motion_api', public=False, permission_classes=[]))
]