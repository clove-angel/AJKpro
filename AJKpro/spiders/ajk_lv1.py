# !/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
from fake_useragent import UserAgent
from AJKpro.tools.pro import PRO_ZM
from lxml import  etree
from scrapy import cmdline
class AJK_lv1(object):
    def __init__(self):
        self.base_url = 'https://chongqing.anjuke.com/?from=navigation'

    def parse_url(self):
        pro = PRO_ZM().get_zm()[0]
        ua = UserAgent()
        headser = {'user-agent':ua.random}
        proxy = {'https':'https://'+pro}
        print('baseUrl:',self.base_url)
        response = requests.get(self.base_url,headers=headser,proxies=proxy)
        response.encoding = 'utf-8'
        html = etree.HTML(response.text)
        return html

    def urls_lv1(self):
        html = self.parse_url()
        urls = html.xpath('//*[@class="L_tabsnew"]/li[position()>1 and position()<6]/a/@href')  # 1新房 2二手房 3租房 4商铺等
        item = {} #获取一级页面urls
        for t,url in zip(range(1,len(urls)+1),urls):
            item[str(t)] = url
        print(item)
        return item

    def newH(self):
        url1 = self.urls_lv1()['1']
        self.base_url = url1
        html = self.parse_url()
        areas = html.xpath('//*[@class="item-list area-bd"]/div[1]/a/text()')
        urls = html.xpath('//*[@class="item-list area-bd"]/div[1]/a/@href')
        l = []
        for area,url in zip(areas,urls):
            Nitem = {}
            Nitem[area]=url
            l.append(Nitem)
        print(l)
        return l

    def secondH(self):
        url2 = self.urls_lv1()['2']
        self.base_url = url2
        html = self.parse_url()
        areas = html.xpath('//*[@class="region region-line2"]/li[position()>1]/a/text()')
        urls = html.xpath('//*[@class="region region-line2"]/li[position()>1]/a/@href')
        l = []
        for area, url in zip(areas, urls):
            Nitem = {}
            Nitem[area] = url
            l.append(Nitem)
        # print(l)
        return l

    def rantH(self):
        url3 = self.urls_lv1()['3']
        self.base_url = url3
        html = self.parse_url()
        areas = html.xpath('//*[@class="item-list area-bd"]/div[1]/a/text()')
        urls = html.xpath('//*[@class="item-list area-bd"]/div[1]/a/@href')
        l = []
        for area, url in zip(areas, urls):
            Nitem = {}
            Nitem[area] = url
            l.append(Nitem)
        print(l)
        return l

    def Shop(self):
        url4 = self.urls_lv1()['4']
        self.base_url = url4
        html = self.parse_url()
        areas = html.xpath('//*[@class="item-list area-bd"]/div[1]/a/text()')
        urls = html.xpath('//*[@class="item-list area-bd"]/div[1]/a/@href')
        l = []
        for area, url in zip(areas, urls):
            Nitem = {}
            Nitem[area] = url
            l.append(Nitem)
        print(l)
        return l


    def run(self):
        self.urls_lv1()
        self.newH()


if __name__ == '__main__':
    A = AJK_lv1()
    A.run()


