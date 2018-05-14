# -*- coding: utf-8 -*-
from urllib import request

from bs4 import BeautifulSoup


# 慕课网爬虫类
class MoocCrawler(object):

    def crawl(self):
        root_url = 'https://www.icourse163.org/'
        html = request.urlopen(root_url)  # 读html
        soup = BeautifulSoup(html, 'html.parser')  # 构造BeautifulSoup
        print(soup.body)


if __name__=='__main__':
    moocCrawler = MoocCrawler()
    moocCrawler.crawl()