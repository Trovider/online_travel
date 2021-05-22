from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'online_travel/select_country.html')


def select_area(request):
    return render(request, 'online_travel/select_area.html')


def bookmark(request):
    return render(request, 'online_travel/bookmark.html')


def mypage(request):
    return render(request, 'online_travel/mypage.html')




