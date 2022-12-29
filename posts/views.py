# from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerialisers
# Create your views here.

class PostList(generics.ListAPIView):
    permission_classes = (permissions.IsAunthenticated)
    queryset = Post.objects.all()
    serializer_class = PostSerialisers

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    (permissions.IsAunthenticated)
    queryset = Post.objects.all()
    serializer_class = PostSerialisers
