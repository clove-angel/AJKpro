# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from AJKpro.items import AjkNhItem, AjkShItem, AjkLlShItem
class AjkproPipeline:
    def process_item(self, item, spider):
        return item


class AjkMysqlPipeline:

    def open_spider(self,spider):
        print('打开数据库链接')
        self.conn = pymysql.connect(host='120.25.3.117', user='datarender', passwd="datarender123", db='zc_yuqing')
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):
        if isinstance(item, AjkNhItem):
            sql = 'insert into 58tcxf_spbyb (NH_name,NH_at,NH_pr,NH_type,NH_ba,,NH_area,NH_str,NH_addr,NH_ss,NH_use,NH_view,NH_url,Source) values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");' % (item['NH_name'],item['NH_at'],item['NH_pr'],item['NH_type'],item['NH_ba'],item['NH_area'],item['NH_str'],item['NH_addr'],item['NH_ss'],item['NH_use'],item['NH_view'],item['NH_url'],item['Source']
)

        elif isinstance(item, AjkLlShItem):
            sql = 'insert into 58tcRH (R_tp,R_title,R_pr,R_type,R_ba,R_url,R_area,R_name,Source,Page,R_A) values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");' % (
            item['R_tp'], item['R_title'], item['R_pr'], item['R_type'], item['R_ba'], item['R_url'], item['R_area'],
            item['R_name'], item['Source'], item['Page'], item['R_A'])

        elif isinstance(item,AjkLlShItem):
            pass

        elif isinstance(item, TCshItem):
            sql = 'insert into 58tcSH (S_title,S_totp,S_avgp,S_type,S_ba,S_url,S_area,S_address,S_name,Source,Page,S_A) values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");' % (
            item["S_title"], item["S_totp"], item["S_avgp"], item["S_type"], item["S_ba"], item["S_url"],
            item["S_area"], item["S_address"], item["S_name"], item["Source"], item["Page"], item["S_A"])

        elif isinstance(item, TCshopItem):
            sql = 'insert into 58tcSH (S_title,S_totp,S_avgp,S_type,S_ba,S_url,S_area,S_address,S_name,Source,Page,S_A) values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");' % (
            item["S_title"], item["S_totp"], item["S_avgp"], item["S_type"], item["S_ba"], item["S_url"],
            item["S_area"], item["S_address"], item["S_name"], item["Source"], item["Page"], item["S_A"])
        elif isinstance(item, TCshllItem):
            sql = 'insert into 58tcSH (S_name,L_lng,L_lat,L_glng,L_glat,Page,S_A) values ("%s","%s","%s","%s","%s","%s","%s");' % (
                item["S_name"], item["L_lng"], item["L_lat"], item["L_glng"], item["L_glat"], item["Page"], item['S_A'])
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            print('插入数据库出错')
            print(sql)
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
        print('入库完成')




