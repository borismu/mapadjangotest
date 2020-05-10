from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'user'

urlpatterns = [
    path('', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(), {
         'template_name': 'user/login.html'}, name='login'),
    path('logout', auth_views.LogoutView.as_view(),
         name='logout'),
    path('user', views.user_info, name='userinfo'),
]
