# -*- coding: utf-8 -*-

"""WebApps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crawler import  views as crawler_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # crawler
    path('crawler/console.page', crawler_views.console_page),  # 爬虫控制台
    path('crawler/crawler.do', crawler_views.crawler_do),  # 爬虫动作
]
