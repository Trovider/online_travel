from django.shortcuts import render, redirect
from .serializers import BookmarkSerializer
from rest_framework import generics
from .models import Bookmark


class BookmarkView(generics.ListCreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer


def index(request):
    return render(request, 'online_travel/select_country.html')


def select_area(request):
    return render(request, 'online_travel/select_area.html')


def bookmark(request):
    return render(request, 'online_travel/bookmark.html')


def mypage(request):
    return render(request, 'online_travel/mypage.html')



