from django.shortcuts import render
from .models import Link
from .serilizers import LinkSerializer
from rest_framework.generics import ListAPIView
from rest_framework .generics import CreateAPIView
from rest_framework .generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView

class PostListApi(ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostCreateApi(CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDetailApi(RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostUpdate(UpdateAPIView):
    queryset = Link.object.filter(active=True)
    serializer_class = LinkSerializer

class PostDelete(DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer




