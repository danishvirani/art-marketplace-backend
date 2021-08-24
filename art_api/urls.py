from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/art', views.ArtList.as_view(), name='art_list'),
    path('api/art/<int:pk>', views.ArtDetail.as_view(), name='art_detail'),
    path('api/artist', views.ArtistList.as_view(), name='artist_list'),
    path('api/artist/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('api/users', views.UserList.as_view(), name='user_list'),
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('api/users/login', csrf_exempt(views.check_login), name="check_login"),
]
