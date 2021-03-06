from django.urls import path, include
from . import views

app_name = 'online_travel'

urlpatterns = [
    path('', views.index, name='index'),
    path('GO/', views.index),
    path('bookmark/', views.bookmark_page, name='bookmark'),
    path('mypage/', views.mypage, name='mypage'),
    path('<country>/', views.select_area),
    path('<country>/<area>/', views.recommend),
    path('<country>/<area>/<spot>/', views.recommend_detail),
]