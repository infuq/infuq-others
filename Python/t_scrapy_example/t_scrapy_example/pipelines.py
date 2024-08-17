# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import openpyxl
import pymysql

class DbPipeline:

    def __init__(self):
        self.conn = pymysql.connect(host="localhost",
                                    port=3306,
                                    user="root",
                                    passwd="9527",
                                    db="db0")
        self.cursor = self.conn.cursor()
        self.data = []

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        if len(self.data) > 0:
            self._write_db()
        self.conn.close()

    def process_item(self, item, spider):
        title = item.get('item', '')
        rating = item.get('rating') or ''
        self.data.append((title, rating))
        if len(self.data) == 20:
            self._write_db()
            self.data.clear()

        return item

    def _write_db(self):
        self.cursor.executemany(
            'insert into t() values(%s, %s)',
            self.data
        )
        self.conn.commit()


class ExcelPipeline:

    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title = '影评'
        self.ws.append(('标题', '评分'))

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.wb.save('movie.xlsx')

    def process_item(self, item, spider):

        title = item.get('title', '')
        rating = item.get('rating') or ''
        self.ws.append((title, rating))
        return item
