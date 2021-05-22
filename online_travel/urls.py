from django.urls import path, include
from . import views

app_name = 'online_travel'

urlpatterns = [
    path('', views.index, name='index'),
    path('select_area/', views.select_area, name='select_area'),
    path('bookmark/', views.bookmark, name='bookmark'),
    path('mypage/', views.mypage, name='mypage'),
    path('api/', views.BookmarkView.as_view())
]