from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, CommentViewSet, GroupViewSet
from rest_framework.authtoken import views
router = routers.DefaultRouter()
router.register(
    r'api/v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router.register('api/v1/posts', PostViewSet)
router.register('api/v1/groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
