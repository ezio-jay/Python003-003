# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class MaoyanPipeline:
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_time = item['movie_time']
        sql = """
        insert into movie (movie_name,movie_type,movie_date) values (%s,%s,%s)
        """
        try:
            self.cursor.excute(sql,(movie_name, movie_type, movie_time))
            self.connect.commit()
        except Exception as f:
            self.connect.rollback()
            print(f)
        return item
    def open_spider(self,spider):
        #   连接数据库,提交作业时将密码修改
        self.connect = pymysql.connect(host = "localhost", user = 'root', passwd = "xxxx", db = "train")
        # 得到游标
        self.cursor = self.connect.cursor()
        print("成功连接到数据库")
    def close_spider(self,spider):
        #关闭游标和连接
        self.cursor.close()
        self.connect.close()