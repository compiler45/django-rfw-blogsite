from django.urls import include, path
from rest_framework.routers import SimpleRouter

from posts.views import PostViewSet, UserViewSet


router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('', PostViewSet, base_name='posts')

urlpatterns = router.urls
