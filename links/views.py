from django.shortcuts import render
from .models import Link
from .serilizers import LinkSerializer
from  rest_framework.generics import ListAPIView


class PostListApi(ListAPIView):
    queryset = Link.objects.filter(active=True)

    serializer_class = LinkSerializer

