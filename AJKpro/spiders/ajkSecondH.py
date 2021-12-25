import re

import scrapy
from AJKpro.spiders.ajk_lv1 import AJK_lv1
from AJKpro.items import AjkShItem , AjkLlShItem
class AjksecondhSpider(scrapy.Spider):
    name = 'ajkSecondH'
    allowed_domains = ['anjuke.com']
    # start_urls = ['http://anjuke.com/']

    def start_requests(self):
        # Surls = AJK_lv1().secondH()
        Surls =[{'渝北': 'https://chongqing.anjuke.com/sale/yubei/'}, {'南岸': 'https://chongqing.anjuke.com/sale/nanana/'}, {'沙坪坝': 'https://chongqing.anjuke.com/sale/shapingba/'}, {'九龙坡': 'https://chongqing.anjuke.com/sale/jiulongpo/'}, {'江北': 'https://chongqing.anjuke.com/sale/jiangbei/'}, {'渝中': 'https://chongqing.anjuke.com/sale/yuzhong/'}, {'巴南': 'https://chongqing.anjuke.com/sale/banan/'}, {'北碚': 'https://chongqing.anjuke.com/sale/beibei/'}, {'万州': 'https://chongqing.anjuke.com/sale/wanzhouqu/'}, {'璧山': 'https://chongqing.anjuke.com/sale/bishanqu/'}, {'永川': 'https://chongqing.anjuke.com/sale/yongchuanqu/'}, {'合川': 'https://chongqing.anjuke.com/sale/hechuanqu/'}, {'大渡口': 'https://chongqing.anjuke.com/sale/dadukou/'}, {'江津': 'https://chongqing.anjuke.com/sale/jiangjinqu/'}, {'铜梁': 'https://chongqing.anjuke.com/sale/tongliangqu/'}, {'涪陵': 'https://chongqing.anjuke.com/sale/fulingqu/'},
 {'长寿': 'https://chongqing.anjuke.com/sale/changshouqu/'}, {'荣昌': 'https://chongqing.anjuke.com/sale/rongchangqu/'}, {'潼南': 'https://chongqing.anjuke.com/sale/tongnanqu/'}, {'大足': 'https://chongqing.anjuke.com/sale/dazhuqu/'}, {'开州': 'https://chongqing.anjuke.com/sale/kaizhouqukaixian/'}, {'垫江': 'https://chongqing.anjuke.com/sale/dainjiangxian/'}, {'綦江':
 'https://chongqing.anjuke.com/sale/qijiangqu/'}, {'南川': 'https://chongqing.anjuke.com/sale/nanchuanqu/'}, {'梁平': 'https://chongqing.anjuke.com/sale/liangpingxian/'}, {'万盛': 'https://chongqing.anjuke.com/sale/wansheng/'}, {'奉节': 'https://chongqing.anjuke.com/sale/fengjiexian/'}, {'云阳': 'https://chongqing.anjuke.com/sale/yunyangxian/'}, {'丰都': 'https://chongqing.anjuke.com/sale/fengduxian/'}, {'彭水': 'https://chongqing.anjuke.com/sale/pengshuimiaozutujiazuzizhixian/'}, {'忠县': 'https://chongqing.anjuke.com/sale/zhongxian/'}, {'秀山': 'https://chongqing.anjuke.com/sale/xiushantujiazumiaozuzizhixian/'}, {'黔江': 'https://chongqing.anjuke.com/sale/qianjiangqu/'}, {'武隆': 'https://chongqing.anjuke.com/sale/wulongxian/'},
 {'巫山': 'https://chongqing.anjuke.com/sale/cqwushanxian/'}, {'石柱': 'https://chongqing.anjuke.com/sale/shizhutujiazuzizhixian/'}, {'酉阳':'https://chongqing.anjuke.com/sale/youyangtujiazumiaozuzizhixian/'}, {'城口': 'https://chongqing.anjuke.com/sale/chengkouxian/'}, {'巫溪': 'https://chongqing.anjuke.com/sale/wuxixian/'}]
        for Surl in Surls:
            key = list(Surl.keys())[0]
            url = Surl[key]
            headers = {"Referer": url}
            yield scrapy.Request(url, callback=self.parse,headers=headers)
            break

    def parse(self, response):
        surls = response.xpath('//*[@class="region region-line3"]/li[position()>1]/a/@href') #获取street
        print("surls:",surls)
        for surl in surls:
            url = surl.extract()
            print('URL:',url)
            headers = {"Referer": url}
            yield scrapy.Request(url,callback=self.parselv1,headers=headers,meta={'url':url})
            break

    def parselv1(self,response): #获取页面数
        base_url = response.meta['url']
        pages = response.xpath('//*[@class="page-item last"]/a/text()')
        print("pages",pages)
        if len(pages) == 0:
            print('只有一页！！！')
            url = base_url
            headers = {"Referer": url}
            yield scrapy.Request(url,callback=self.parse_data,headers=headers,meta={'page':1})
        else:
            print('有很多页！！！')
            for page in range(1,len(pages)+2):
                url = base_url.replace('?from=SearchBar',f'p{page}/?from=SearchBar')
                print(url)
                yield scrapy.Request(url, callback=self.parse_data, meta={'page': page})
                break
    def parse_ll(self, response):
        print(response)
        print('获取经纬度!!!')

    def parse_data(self,response):
        print('获取房屋信息!!!')
        self.parse_ll(response)
        item = AjkShItem()
        base_xp = response.xpath('//*[@class="list"]/div/a/div[2]')
        S_urls = response.xpath('//*[@class="list"]/div/a/@href')
        S_names = base_xp.xpath('./div[1]/section/div[2]/p/text()')
        S_titles = base_xp.xpath('./div[1]/div[1]/h3/text()')
        S_types = base_xp.xpath('./div[1]/section/div[1]/p[1]')
        S_bas = base_xp.xpath('./div[1]/section/div[1]/p[2]/text()')
        # S_ots = base_xp.xpath('./div[1]/section/div[1]/p[3]/text()') #朝向
        S_As = base_xp.xpath('./div[1]/section/div[2]/p[2]/span[1]/text()')
        S_areas = base_xp.xpath('./div[1]/section/div[2]/p[2]/span[2]/text()')
        S_addrs = base_xp.xpath('./div[1]/section/div[2]/p[2]/span[3]/text()')
        S_totps = base_xp.xpath('./div[2]/p[1]/span[1]/text()')
        S_avgps = base_xp.xpath('./div[2]/p[2]/text()')

        for url, na, title, type, ba, A, area, addr, totp, avgp in zip(S_urls, S_names, S_titles, S_types, S_bas, S_As,
                                                                       S_areas, S_addrs, S_totps, S_avgps):
            item['S_title'] = title.extract()  # 推荐
            item['S_totp'] = totp.extract()  # 总价 W
            item['S_avgp'] = avgp.extract().replace('元/㎡', '')  # 单价 元/㎡
            ty = (type.xpath('string(.)')).extract()[0]
            item['S_type'] = ty  # 户型
            item['S_ba'] = ba.extract().replace('㎡', '').split()[0]  # 建筑面积
            item['S_url'] = (url.extract()).split('&lg=https')[0]  # 楼盘详情页
            item['S_area'] = area.extract()  # 楼盘区域
            item['S_address'] = addr.extract()  # 地址
            item['S_name'] = na.extract()  # 楼盘名称
            item['Page'] = response.meta['page']
            item['S_A'] = A.extract()  # 区
            item['Source'] = self.allowed_domains[0]  # 来源地址
            print(item)
            # yield item


            # item = AjkLlShItem()
            # ll_datas = re.findall()
            # for ll_data in ll_datas:
            #     item['ll_name'] =
            #     item['lng'] =
            #     item['lat'] =
            #     item['glng'] =
            #     item['glat'] =