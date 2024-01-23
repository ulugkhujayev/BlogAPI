from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserViewSet

# from .views import PostList, PostDetail,

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
]


# urlpatterns = [
#     path("<int:pk>", PostDetail.as_view(), name="post_detail"),
#     path("", PostList.as_view(), name="post_list"),
# ]
