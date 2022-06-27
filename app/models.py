
from django.db import models
from django.conf import settings

from rest_framework.authtoken.models import Token



class AuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(AuditModel):
    caption = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img = models.ImageField(height_field=None, width_field=None, max_length=100, default="default.jpg")

    def __str__(self) -> str:
        return self.caption


class Comment(AuditModel):
    text = models.CharField(max_length=500)
    post = models.ForeignKey(Post, related_name= "comments",on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.user.username + " : " + self.text


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")

    def __str__(self):
        return "Like from" + self.user.username + "to" + self.post

