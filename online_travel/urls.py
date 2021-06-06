from django.conf.urls import url
from django.urls import path, include
import parser
from . import views

app_name = 'online_travel'

urlpatterns = [
    path('', views.index, name='index'),
    path('bookmark/', views.bookmark, name='bookmark'),
    path('mypage/', views.mypage, name='mypage'),
    path('<country>/', views.select_area),
    path('<country>/<area>/', views.recommend),
    path('<country>/<area>/<spot>/', views.recommend_detail),
    path('password/', views.password_edit_view, name='password_edit'),

]