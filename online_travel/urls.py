from django.urls import path, include
from . import views

app_name = 'online_travel'

urlpatterns = [
    path('', views.index, name='index'),
    path('bookmark/', views.bookmark, name='bookmark'),
    path('mypage/', views.mypage, name='mypage'),
    path('<country>/', views.select_area),
]