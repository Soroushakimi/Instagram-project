
from django.db import IntegrityError
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import authentication, permissions, status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser


#from insta.user import views


from .models import Post, Comment, Like
from .serializers import CommentSerializer, LikeSerializer, PostListSerializers, PostDetailSerializers
from user import signals
from user.models import Following

# class BasePostViewset(viewsets.ModelViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return super().get_queryset().filter(user=self.request.user)


# class PostViewset(BasePostViewset):
#     queryset = Post.objects.all()
    # serializer_class = PostDetailSerializers



class PostListView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get(self, request:Request):
        following = Following.objects.get(id = request.user.id).followings.all()
        qs = Post.objects.filter(user__in= following)
        serializer = PostListSerializers(qs, many=True, context={'request': request})
        return Response (serializer.data)

    def post(self, request:Request):
        serializer = PostListSerializers(data=request.data, context={'user':request.user})
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({"status": "success", "message": "ok shod"}, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({"status": "error", "error_message": "hamchin posti ghablan dashti"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors)



class PostDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializers

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class CommentViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

