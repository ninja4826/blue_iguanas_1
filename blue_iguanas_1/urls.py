"""blue_iguanas_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.conf.urls import include, url
# from django.contrib import admin
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
# from todo import views
from todo import urls

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^users/$', urls.user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', urls.user_detail, name='user-detail'),
    url(r'^users/me$', urls.user_me, name='user-me'),
    url(r'^tasks/$', urls.task_list, name='task-list'),
    url(r'^tasks/(?P<pk>[0-9]+)/$', urls.task_detail, name='task-detail'),
    url(r'^token_auth/', obtain_jwt_token),
    url(r'^token_refresh/', refresh_jwt_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)