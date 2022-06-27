from django.contrib import admin

from .models import Profile, Following, Follower


admin.site.register(Following)
admin.site.register(Follower)

class FollowingInline(admin.StackedInline):
    model = Following

class FollowerInline(admin.StackedInline):
    model = Follower

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        FollowingInline,
        FollowerInline
    ]