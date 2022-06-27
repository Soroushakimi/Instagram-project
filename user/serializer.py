
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model

from user.models import Profile, Following, Follower

from rest_framework import serializers

User = get_user_model()

class ProfileListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = "__all__"


class FollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Following
        fields = ("followings",)
        read_only_fields = ('followings',)

    def create(self, validated_data):
        print("---------------------")
        user = Following.objects.get(profile__user = self.context["profile__user"])
        follow = User.objects.get(id=self.context["user_id"])
        user.followings.add(follow)
        user.save()
        return user


