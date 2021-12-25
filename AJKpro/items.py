# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AjkproItem(scrapy.Item):

    pass


class AjkNhItem(scrapy.Item):
    NH_name = scrapy.Field()  # 楼盘名称
    NH_at = scrapy.Field()  # 楼盘售卖方式 均价\总价
    NH_pr = scrapy.Field()  # 价格
    NH_type = scrapy.Field()  # 户型
    NH_ba = scrapy.Field()  # 建筑面积
    NH_ss = scrapy.Field()  # 售卖状态
    NH_use = scrapy.Field()  # 房屋类型 住宅\公寓\商住
    NH_view = scrapy.Field()  # 看房状态
    NH_url = scrapy.Field()  # 楼盘详情链接
    Source = scrapy.Field()  # 来源地址
    # NH_address = scrapy.Field()  # 楼盘地址
    NH_area = scrapy.Field()
    NH_str = scrapy.Field()
    NH_addr = scrapy.Field()

    pass

class AjkShItem(scrapy.Item):
    S_title = scrapy.Field()  # 推荐
    S_totp = scrapy.Field()  # 总价
    S_avgp = scrapy.Field()  # 均价
    S_type = scrapy.Field()  # 户型
    S_ba = scrapy.Field()  # 建筑面积
    S_url = scrapy.Field()  # 楼盘详情页
    S_area = scrapy.Field()  # 罗盘区域
    S_address = scrapy.Field()  # 楼盘地址
    S_name = scrapy.Field()  # 楼盘名称
    Source = scrapy.Field()  # 来源
    Page = scrapy.Field()  # 页码
    S_A = scrapy.Field()  # 区

class AjkLlShItem(scrapy.Item):
    ll_name = scrapy.Field()
    lng = scrapy.Field()
    lat = scrapy.Field()
    glng = scrapy.Field()
    glat = scrapy.Field()
    pass




