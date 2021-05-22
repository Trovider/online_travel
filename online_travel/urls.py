from django.urls import path
from . import views

app_name = 'online_travel'

urlpatterns = [
    path('', views.index, name='index'),
    path('select_area/', views.select_area, name='select_area'),
    path('bookmark/', views.bookmark, name='bookmark'),
    path('mypage/', views.mypage, name='mypage'),
]