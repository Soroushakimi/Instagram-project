
from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import ProfileListView, FollowingListView

router = DefaultRouter()
router.register("followings", FollowingListView, basename="following")


urlpatterns =[
    path("profile-list/", ProfileListView.as_view(), name="profile-list"),
    # path("following-list/", FollowingListView.as_view(), name="following-list"),

] + router.urls
