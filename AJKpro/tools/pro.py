#!/usr/bin/env python
# -*- coding:utf-8 -*-


import requests
import time
from fake_useragent import UserAgent

class PRO_DLY(object):
    def __init__(self):
        # url = 'https://www.baidu.com'
        # url='https://2021.ip138.com/'
        self.Vfurl = 'http://icanhazip.com'
        # self.Vfurl = 'https://2021.ip138.com/'
        self.proxyusernm = "hclove"        #代理帐号
        self.proxypasswd = "hc654321"        #代理密码
        #name = input();
        self.T = True
    #验证代理ip有效性
    def get_pAddress(self):
        response = requests.get('http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=0&port=1&pack=194329&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=')
        ad = response.text
        addr = ad.split(':')[0]
        port = ad.split(':')[1]
        return addr


    def pro_verification(self):
        proxyaddr = self.get_pAddress()  #代理IP地址
        proxyport = 57114 #代理IP端口
        proxyurl = "http://" + self.proxyusernm + ":" + self.proxypasswd + "@" + proxyaddr + ":" +\
                   "%d" % proxyport
        pro = {'http':proxyurl,'https':proxyurl}
        ua = UserAgent()
        # t1 = time.time()
        try:
            r = requests.get(self.Vfurl,proxies=pro,headers={
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding":"gzip, deflate",
                "Accept-Language":"zh-CN,zh;q=0.9",
                "Cache-Control":"max-age=0",
                "User-Agent":ua.random})
            r.encoding='gb2312'
            self.T = False
        except Exception as e:
            print('代理ip过期:',e)
            self.T = True
        # t2 = time.time()
        # print("时间差:" , (t2 - t1));
        return  pro

    def run(self):
        while self.T:
            p = self.pro_verification()
        return p





class PRO_ZM(object):
    def __init__(self):
        pass

    def get_zm(self):
        time.sleep(1.5)
        # url = 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
        url = 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=0&port=1&pack=194329&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
        html = requests.get(url)
        html = html.text
        ips = html.split('\r\n')
        ip = list(filter(None,ips))
        return ip




# if __name__ == '__main__':
#     p = PRO_ZM()
#     ip = p.get_zm()
#     print(ip)
#








