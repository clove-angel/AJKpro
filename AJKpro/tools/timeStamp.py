#!/usr/bin/env python
# -*- coding:utf-8 -*-
import base64
import random
import time
import zlib
from MTpro.tools.EDcryption import ED
from urllib import parse
class TS(object):

    def __init__(self):
        # self.payload = {"cityName": "重庆",
        #            "cateId": "0",
        #            "areaId": "0",
        #            'sort': '',
        #            'dinnerCountAttrId': '',
        #            'page':'',
        #            "userId": "805676599",
        #            "uuid": "a81076cc50304bd1a2b0.1636696742.1.0.0",
        #            "platform": "1",
        #            "partner": "126",
        #            "originUrl": "https://cq.meituan.com/meishi/",
        #            "riskLevel": "1",
        #            "optimusCode": "10",
        #            '_token': 'eJx1T9lugkAU/Zd5lciAMDAmfXBBZKuCUloaHxBGQFnKJkrTf++YtA99aHKTs9yTk3s/Qa1FYMpBiCFkwJXUYAq4MRwjwIC2oRs0QRghTuBFETMg/OshKDPgWL8swfRdRBKDET48DIfqdw7zkOGgDA/MLxco5wU6j5RGQyBp249myrJhNc5J2nZBMQ7LnKW8SVKWHvFPANCGfE8bKF5+MPjB9ldb9Bla0aRxQRnR++y85zazQbETMtr11cvkamWogXHnLsqLY4Vz/RrYnjG0/v6mCrFuh7t1Z8tKaxk6KkSJDD3y5YUguHO0YtO1wfdWHp7lU4HxSbrXSqFl2w/PE1dEJa7n7fNViTN3uYkXZWgOCit3VadlHVbtI1smz6vATzmTL8pXA9/ceUtIpZg7EUO/diqPU8miiroQDVvMOkYwigJPv1XZSRqdz0ufdyWzzCqzJ2unV++44GfbZGL1G12cq1I3ier18BY5aiwcI3MkZztXewJf362xllI='}
        self.token = 'eJx1T9tuqkAU/Zd5lcgwwMCY9KEqIrejoJRzaPqAMAKWS7mJ0vTfO03alyYn2cm67JWVvd9BayRgIUBIIOTAlbZgAYQ5nGPAgb5jGywqUEJEVhUkciD+5WGVA6f2aQ0WzwQijmDy8mV4TD8LBEFOgCp84X64xDiS2HylDBYCWd+/dQuej5t5SfN+iKp5XJc8412W8+yI/wQAayiPrIHh6zdG39j/aIc9wyq6PK0Yo+ZYXI7C7nHS3IzODmPzJF6dAncwHfxV/eo58dK8Rm5gTX14vOlSarrxYTu4qtY7lokrWaHTiEN1JUn+Em/4fGuh0Snji3quCDkr91arjGL/FgTyhurUD4JjualJ4a936aqO7Unj1aEZjGIgunvi6+zPJgpzwUZV/dciN3/ZU9po9kEmMGy9JhB0umqSIcbTnvCeFc2SKDBvTXFWZpfLOkS+YtdFY4906436nVTocZ+Jzrgz5aWuDGLSbqd/iaen0imxZ2px8I0H8PEJpNWWTQ=='
        #获取新的token值
    def get_token(self):
        ed = ED()
        t = ed.decryption(self.token)  #解码获取字典
        t['ts'] = int(time.time()*1000) #更改时间戳
        t['cts'] = int(time.time()*1000)+random.randint(1,100)
        en = ed.encryption(t) #重新加密并返回加密token
        entok = parse.quote_plus(en) #返回经过url编码后的tonken
        return entok



if __name__ == '__main__':
    t = TS()
    print(t.get_token())
