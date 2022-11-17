from django.urls import include, path
from rest_framework import routers
# from django.conf import settings

from .views import (
    PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
)

v2_router = routers.DefaultRouter()

v2_router.register('posts', PostViewSet)
v2_router.register('groups', GroupViewSet)
v2_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
v2_router.register(
    'follow', FollowViewSet,
    basename='follow'
)

urlpatterns = [
    path('v1/', include('djoser.urls')),  # регистрируем/проверяем юзера
    path('v1/', include('djoser.urls.jwt')),  # получаем/создаем токен
    path('v1/', include(v2_router.urls)),  # эндпоинты
]
