from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('comment/', CommentViewSet.as_view({'post': 'create'}), name='comment'),
    path('anime/<pk>/', AnimeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='anime_detail'),
    path('anime/', AnimeViewSet.as_view({'get': 'list', 'post': 'filter'}), name='anime'),
    path('parse/', ParseAnimesView.as_view(), name='parse_movies'),

    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
