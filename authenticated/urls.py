from django.urls import path
from .views import PostsList, PostsListAll, PostDetail

urlpatterns = [
    path('', PostsListAll.as_view(), name='blog'),
    path('post/<int:pk>', PostDetail.as_view(), name="post"),
    path('profile/', PostsList.as_view(), name='profile')
]