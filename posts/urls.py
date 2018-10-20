from django.urls import include, path

from posts.views import PostList, PostDetail


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
