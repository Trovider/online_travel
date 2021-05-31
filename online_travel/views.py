from django.shortcuts import render, redirect, get_list_or_404
from .models import Bookmark, Spot


def index(request):
    return render(request, 'online_travel/select_country.html')


def select_area(request, country):

    area = get_list_or_404(Spot.objects.filter(country_name=country))
    return render(request, 'online_travel/select_area.html', {'area': area})


def bookmark(request):
    return render(request, 'online_travel/bookmark.html')

def mypage(request):
    return render(request, 'online_travel/mypage.html')