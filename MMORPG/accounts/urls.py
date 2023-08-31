from django.urls import path
from .views import IndexView


app_name = 'profile'
urlpatterns = [
    path('', IndexView.as_view(), name='profile_index'),
]
