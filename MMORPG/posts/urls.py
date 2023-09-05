from django.urls import path
from .views import PostsList, PostDetail, PostDelete, PostCreate, PostUpdate, PostsProfileList, ResponseCreate, MyResponsesList
# У меня в VsCode почему то не переносится строчка автоматически и выдает ошибку импорта, поэтому еще один импорт
from .views import RespondendPublicationList, ViewResponsesDetail, feedback_accept, feedback_no_accept, feedback_delete

app_name = 'posts'
urlpatterns = [
    path('', PostsList.as_view(), name='posts_page'),
    path('add/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/resp', ResponseCreate.as_view(), name='response_create'),
    path('pplist', PostsProfileList.as_view(), name='profile_posts'),
    path('resplist', MyResponsesList.as_view(), name='profile_responses'),
    path('respedlist', RespondendPublicationList.as_view(),
         name='profile_responsed'),
    path('<int:pk>/respdetail', ViewResponsesDetail.as_view(),
         name='response_detail'),
    path('<int:pk>/accept/', feedback_accept, name='feedback_accept'),
    path('<int:pk>/noaccept/', feedback_no_accept, name='feedback_no_accept'),
    path('<int:pk>/respdelete/', feedback_delete, name='feedback_delete'),
]
