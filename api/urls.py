from django.urls import path, re_path, include
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view # new
from drf_yasg import openapi # new

schema_view = get_schema_view( # new
    openapi.Info(
        title="Blog API",
        default_version="v1",
        description="A sample API for learning DRF",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hello@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('comment/', CommentViewSet.as_view({'post': 'create'}), name='comment'),
    path('thing/<pk>/', ThingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='thing_detail'),
    path('thing/', ThingViewSet.as_view({'get': 'list', 'post': 'create'}), name='thing'),
    path('parse/', ParseThingsView.as_view(), name='parse_movies'),

    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
