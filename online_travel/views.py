from django.shortcuts import render, redirect, get_list_or_404
from .models import Spot
from .data import parse_blog


def index(request):
    return render(request, 'online_travel/select_country.html')


def select_area(request, country):
    area = get_list_or_404(Spot.objects.filter(country_name=country).values('area_name', 'country_name').distinct())
    return render(request, 'online_travel/select_area.html', {'area': area})


def recommend(request, country, area):
    title_list = Spot.objects.order_by('spot_name')
    spot = get_list_or_404(Spot.objects.filter(area_name=area))
    #parse_blog(country, area) #db에 저장됐으면 빼고 돌려도 됨
    context = {'spot': spot, 'title_list': title_list}
    return render(request, 'online_travel/recommend.html', context)


def recommend_detail(request, country, area, spot):
    spot_detail = get_list_or_404(Spot.objects.filter(spot_name=spot))
    return render(request, 'online_travel/recommend_detail.html', {'spot_detail': spot_detail})


def bookmark(request):
    return render(request, 'online_travel/bookmark.html')


def mypage(request):
    return render(request, 'online_travel/mypage.html')
