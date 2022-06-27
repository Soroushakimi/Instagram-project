
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import authentication, permissions, generics
from rest_framework.generics import GenericAPIView, mixins
from rest_framework.response import Response
from rest_framework import status

from .serializer import FollowingSerializer, ProfileListSerializer
from .models import Following, Profile
from user import serializer


class ProfileListView(generics.ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileListSerializer
    queryset = Profile.objects.all()


# class FollowinglistView(generics.ListAPIView):
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = Followinglistserializer
#     queryset = Following.objects.all()

#     def get_queryset(self):
#         return super().get_queryset().filter(profile__user=self.request.user)
    

class FollowingListView(viewsets.ViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        print(request.query_params.get("user_id"))
        serializer = FollowingSerializer(data=request.data, context={"profile__user":request.user, "user_id": request.query_params.get("user_id")})
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response (serializer.errors, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        qs = Following.objects.all().filter(profile__user = request.user)
        serializer = FollowingSerializer(qs, many = True)
        return Response(serializer.data)



