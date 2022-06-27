
from rest_framework import serializers

from .models import Post, Comment, Like



class PostListSerializers(serializers.ModelSerializer):

    class Meta:
       model = Post
       fields = ('caption', 'img')
    
    def create(self, validated_data):
        return Post.objects.create(user=self.context["user"], **validated_data)



class PostDetailSerializers(serializers.ModelSerializer):

    comments = serializers.StringRelatedField(many=True)
    likes = serializers.StringRelatedField(many = True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('text, post')


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('post',)

