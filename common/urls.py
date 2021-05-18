from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('select-country/', views.select_country, name='select-country'),
    path('select-area/', views.select_area, name='select-area'),
    path('bookmark/', views.bookmark, name='bookmark'),
    path('tourpage/', views.tourpage, name='tourpage'),
]