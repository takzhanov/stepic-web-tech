"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from qa import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.new, name='index'),
    url(r'^login/', views.login_view, name='login_view'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^question/(?P<id>\d+)/$', views.question, name='question'),
    url(r'^ask/', views.new_question, name='new_question'),
    url(r'^popular/', views.popular, name='index'),
    url(r'^new/', views.new, name='index'),
    url(r'^time/$', views.time),
]
