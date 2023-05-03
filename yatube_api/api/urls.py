from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet, GroupViewSet, PostViewSet

api_router_v1 = routers.DefaultRouter()
api_router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
api_router_v1.register('posts', PostViewSet, basename='post')
api_router_v1.register('groups', GroupViewSet, basename='group')

urlpatterns = [
    path('v1/', include(api_router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
