from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from dummy import views

schema_view = get_schema_view(
    openapi.Info(
        title="Bubbling Dummy API",
        default_version='v0.1',
        description="This app is used fro demonstration purpose only",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="dimitris.samaras1@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)/$', schema_view.without_ui(cache_timeout=0), name='schema-json-yaml'),
]


urlpatterns += [
    path("", include([
        path("", views.dummy_list, name="dummy-list"),
        path("<int:pk>/", views.dummy_get, name="dummy-list-with-id"),
    ]))
]
