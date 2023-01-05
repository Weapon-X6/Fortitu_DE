import os

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from blog.api.views import PostViewSet, UserDetail, TagViewSet

urlpatterns = [
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if os.getenv("DJANGO_CONFIGURATION") == "Dev":
    url = "http://127.0.0.1:8000/api/v1/"
else:
    url = "https://weaponx.pythonanywhere.com/api/v1/"

schema_view = get_schema_view(
    openapi.Info(
        title="Blango API",
        default_version="v1",
        description="API for Blango Blog",
    ),
    url=url,
    public=True,
)

urlpatterns += [
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
    path("jwt/", TokenObtainPairView.as_view(), name="jwt_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

router = DefaultRouter()
router.register("tags", TagViewSet)
router.register("posts", PostViewSet)

urlpatterns += [
    path("", include(router.urls)),
    path(
        "posts/by-time/<str:period_name>/",
        PostViewSet.as_view({"get": "list"}),
        name="posts-by-time",
    ),
]
