
from django.db import models
from django.conf import settings

from rest_framework.authtoken.models import Token

from app.models import AuditModel


class Profile(AuditModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    photo = models.ImageField(height_field=None, width_field=None, max_length=100, default="default.jpg")
    age = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    # following = models.ManyToManyField("Profile", related_name="followings", null=True, blank=True)
    # followers = models.ManyToManyField("profile", related_name="followed_by", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.username} profile"


class Following(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, unique=True)
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="following", symmetrical=False)

    def __str__(self) -> str:
        return f"{self.profile.user} followings"


class Follower(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, symmetrical=False)

    def __str__(self) -> str:
        return f"{self.profile.user} followers"

