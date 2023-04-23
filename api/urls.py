from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('comment/', CommentViewSet.as_view({'post': 'create'}), name='comment'),
    path('thing/<pk>/', ThingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='thing_detail'),
    path('thing/', ThingViewSet.as_view({'get': 'list', 'post': 'create'}), name='thing'),
    path('parse/', ParseThingsView.as_view(), name='parse_movies'),

    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
