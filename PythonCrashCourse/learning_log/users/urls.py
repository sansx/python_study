
"""定义users的URL模式"""
from django.urls import path,include,re_path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'

urlpatterns = [
    # 主页
    # re_path(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    re_path(r'^logout/$', views.logout_view, name='logout'),
    re_path(r'^register/$', views.register, name='register'),
]