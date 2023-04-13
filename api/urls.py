from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('', ExampleView.as_view(), name='example'),
    path('parse/', ParseMoviesView.as_view(), name='parse_movies'),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
