
from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import CommentViewset, LikeViewset, PostListView, PostDetailView


router = DefaultRouter()
router.register("comment", CommentViewset, basename="comments")
router.register("like", LikeViewset, basename="likes")


urlpatterns =[
    path("post-list/", PostListView.as_view(), name="post_list"),
    path("post-detail/<int:pk>", PostDetailView.as_view(), name="post_detail"),
    # path("post/", BasePostViewset.as_view(), name="post")
] + router.urls
