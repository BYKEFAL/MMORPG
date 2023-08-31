from django.urls import path
from .views import PostsListView, PostDetail, PostDelete, PostCreate, PostUpdate, PostsProfileList


app_name = 'posts'
urlpatterns = [
    path('', PostsListView.as_view(), name='posts_page'),
    path('add/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('pplist', PostsProfileList.as_view(), name='posts_profile'),
]
