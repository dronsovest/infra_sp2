from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import GetConfirmationCode, GetToken, UserViewSet

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet)

router = DefaultRouter()

router.register("users", UserViewSet, basename="users")
router.register("genres", GenreViewSet, basename="genres")
router.register("categories", CategoryViewSet, basename="categories")
router.register("titles", TitleViewSet, basename="titles")
router.register(r"titles/(?P<title_id>\d+)/reviews", ReviewViewSet, basename="reviews")
router.register(
    r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/Comment",
    CommentViewSet,
    basename="Comment",
)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/auth/email/", GetConfirmationCode.as_view()),
    path("v1/auth/token/", GetToken.as_view()),
]
