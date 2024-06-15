from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router.register(
    'follow', FollowViewSet,
    basename='follows'
)

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls))
]
