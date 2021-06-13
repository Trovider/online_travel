from django.shortcuts import render, redirect, get_list_or_404
from .models import Spot, Video, Bookmark
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .data import parse_blog, detail_save


def index(request):
    return render(request, 'online_travel/select_country.html')


def select_area(request, country):
    area = Spot.objects.filter(country_name=country).values('area_name', 'country_name').distinct()
    return render(request, 'online_travel/select_area.html', {'area': area})


def recommend(request, country, area):
    title_list = Spot.objects.order_by('spot_name')

    spot = Spot.objects.filter(area_name=area)
    parse_blog(country, area) #db에 저장됐으면 빼고 돌려도 됨

    spot = get_list_or_404(Spot.objects.filter(area_name=area))
    parse_blog(country, area)

    context = {'spot': spot, 'title_list': title_list}
    return render(request, 'online_travel/recommend.html', context)


def recommend_detail(request, country, area, spot):
    spot_detail = Spot.objects.get(spot_name=spot)
    #detail_save(spot_detail)
    video = Video.objects.filter(spot_name=spot)
    bookmark = Bookmark.objects.filter(spot_name=spot, user=request.user)
    if request.method == 'POST':
        try:
            is_bookmarked = Bookmark.objects.get(spot_name=spot, user=request.user)
        except:
            is_bookmarked = None
        if is_bookmarked:
            is_bookmarked.delete()
        else:
            model_instance = Bookmark(spot_name=spot_detail, user=request.user, memo='입력하세요')
            model_instance.save()
    return render(request, 'online_travel/recommend_detail.html', {'spot_detail': spot_detail, 'video': video, 'bookmark': bookmark})


def bookmark_page(request):
    bookmark = Bookmark.objects.filter(user=request.user)
    return render(request, 'online_travel/bookmark.html', {'bookmark': bookmark})


def mypage(request):
    return render(request, 'online_travel/mypage.html')
