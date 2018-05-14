# -*- coding: utf-8 -*-

from django.shortcuts import render


# Create your views here.

# 控制台
from crawler.crawlers import MoocCrawler


def console_page(request):
    return render(request, 'crawler/console.html', None)


# 爬虫动作
def crawler_do(request):
    try:
        crawler = MoocCrawler()
        crawler.crawl()
    except Exception as e:
        print(e)

