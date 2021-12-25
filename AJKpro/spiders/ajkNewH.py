import scrapy
from AJKpro.spiders.ajk_lv1 import AJK_lv1
from AJKpro.items import AjkNhItem


class AjknewhSpider(scrapy.Spider):
    name = 'ajkNewH'
    allowed_domains = ['anjuke.com']
    # start_urls = ['http://anjuke.com/']

    def start_requests(self):
        # Nurls = AJK_lv1().newH()
        # Nurls = [{'渝北': 'https://cq.fang.anjuke.com/loupan/yubei/'}, {'九龙坡': 'https://cq.fang.anjuke.com/loupan/jiulongpo/'}, {'沙坪坝': 'https://cq.fang.anjuke.com/loupan/shapingba/'}, {'巴南': 'https://cq.fang.anjuke.com/loupan/banan/'}, {'南岸': 'https://cq.fang.anjuke.com/loupan/nanan/'}, {'两江新区': 'https://cq.fang.anjuke.com/loupan/liangjiangxinqu/'}, {'璧山': 'https://cq.fang.anjuke.com/loupan/bishan/'}, {'江北': 'https://cq.fang.anjuke.com/loupan/jiangbei/'}, {'万州': 'https://cq.fang.anjuke.com/loupan/wanzhou/'}, {'北碚': 'https://cq.fang.anjuke.com/loupan/beibei/'}, {'大渡口': 'https://cq.fang.anjuke.com/loupan/dadukou/'}, {'江津': 'https://cq.fang.anjuke.com/loupan/jiangjin/'}, {'渝中': 'https://cq.fang.anjuke.com/loupan/yuzhong/'}, {'重庆周边': 'https://cq.fang.anjuke.com/loupan/chongqingzhoubian/'}, {'永川': 'https://cq.fang.anjuke.com/loupan/yongchuan/'}, {'合川': 'https://cq.fang.anjuke.com/loupan/hechuan/'}, {'大足': 'https://cq.fang.anjuke.com/loupan/dazu/'}, {'涪陵': 'https://cq.fang.anjuke.com/loupan/fuling/'}, {'潼南': 'https://cq.fang.anjuke.com/loupan/tongnan/'}, {'长寿': 'https://cq.fang.anjuke.com/loupan/changshou/'}, {'荣昌': 'https://cq.fang.anjuke.com/loupan/rongchang/'}, {'南川': 'https://cq.fang.anjuke.com/loupan/nanchuan/'}, {'铜梁': 'https://cq.fang.anjuke.com/loupan/tongliang/'}, {'綦江': 'https://cq.fang.anjuke.com/loupan/qijiang/'}, {'武隆': 'https://cq.fang.anjuke.com/loupan/wulong/'}, {'垫江': 'https://cq.fang.anjuke.com/loupan/dianjiang/'}, {'黔江': 'https://cq.fang.anjuke.com/loupan/qianjiang/'}, {'忠县': 'https://cq.fang.anjuke.com/loupan/zhongxian/'}, {'梁平': 'https://cq.fang.anjuke.com/loupan/liangping/'}, {'云阳': 'https://cq.fang.anjuke.com/loupan/yunyang/'}, {'彭水': 'https://cq.fang.anjuke.com/loupan/pengshui/'}, {'丰都': 'https://cq.fang.anjuke.com/loupan/fengdu/'}, {'奉节': 'https://cq.fang.anjuke.com/loupan/fengjie/'}, {'开州': 'https://cq.fang.anjuke.com/loupan/kaizhou/'}, {'石柱': 'https://cq.fang.anjuke.com/loupan/shizhu/'}, {'巫山': 'https://cq.fang.anjuke.com/loupan/wushan/'}, {'巫溪': 'https://cq.fang.anjuke.com/loupan/wuxi/'}, {'万盛': 'https://cq.fang.anjuke.com/loupan/wansheng/'}, {'秀山': 'https://cq.fang.anjuke.com/loupan/xiushan/'}, {'城口': 'https://cq.fang.anjuke.com/loupan/chengkou/'}, {'酉阳': 'https://cq.fang.anjuke.com/loupan/youyang/'}]
        Nurls = [{'渝北': 'https://cq.fang.anjuke.com/loupan/yubei/'}]
        for Nurl in Nurls:
            key = list(Nurl.keys())[0]
            url = Nurl[key]
            yield scrapy.Request(url,callback=self.parse,meta={'url':url})
            break

    def parse(self, response):
        base_url = response.meta['url']
        pages = response.xpath('//*[@class="pagination"]/a[position() < last()]')
        if len(pages) == 0:
            page = 1
            yield scrapy.Request(base_url,callback=self.parse_data,meta={'page':page})

        else:
            for page in range(1,len(pages)+2):
                url = base_url+f'p{page}'
                yield scrapy.Request(url,callback=self.parse_data,meta={'page':page})
                print(url)
                break

    def parse_data(self,response):
        page = response.meta['page']
        item = AjkNhItem()
        html_infos = response.xpath('//*[@class="infos"]')
        html_price = response.xpath('//*[@class="favor-pos"]')
        html_urls = response.xpath('//*[@class="key-list imglazyload"]/div/@data-link')
        for data, price, U in zip(html_infos, html_price, html_urls):
            item['NH_name'] = data.xpath('./a[1]/span/text()').extract()[0]  # 楼盘名称
            item['NH_at'] = price.xpath('./p/text()').extract()[0]  # 楼盘售卖方式 均价\总价
            item['NH_pr'] = ''.join(price.xpath('./p//text()').extract()[-2:]).replace('\n', '').replace(' ', '')  # 价格
            try:
                item['NH_type'] = '/'.join(data.xpath('./a[3]/span[position()<3]/text()').extract())  # 户型
            except Exception as e:
                item['NH_type'] = '无'
                print('户型异常:', e)
            try:
                item['NH_ba'] = (data.xpath('./a[3]/span[@class="building-area"]/text()').extract()[0]).split('：')[
                    -1]  # 建筑面积
            except Exception as e:
                item['NH_ba'] = '未开盘'
                print('建筑面积异常:', e)
            # item['NH_address'] = ' '.join(list(filter(None, (
            #     data.xpath('./a[2]/span/text()').extract()[0].replace('[', '').replace(']', '').split(
            #         '\xa0')))))  # 楼盘地址
            data =' '.join(list(filter(None, (
                data.xpath('./a[2]/span/text()').extract()[0].replace('[', '').replace(']', '').split(
                    '\xa0')))))  # 楼盘地址
            a_list = data.split(' ')
            item['NH_area'] = a_list[0]
            item['NH_str'] = a_list[1]
            item['NH_addr'] = a_list[2]
            item['NH_ss'] = data.xpath('./a[4]/div/i[1]/text()').extract()[0]  # 售卖状态
            item['NH_use'] = data.xpath('./a[4]/div/i[2]/text()').extract()[0]  # 房屋类型 住宅\公寓\商住
            item['NH_view'] = ','.join(data.xpath('./a[4]/div/span/text()').extract())  # 看房状态
            item['NH_url'] = U.extract()
            item['Source'] = self.allowed_domains[0]
            print(item)
        pass

