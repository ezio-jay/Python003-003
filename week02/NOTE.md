学习笔记
#pymql
[pymql官方文档]（https://pypi.org/project/PyMySQL/）
scrapy 数据同步存储到数据库：
```
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
        self.connect = pymysql.connect(host = "localhost", user = 'root', passwd = "Qzj853701521992", db = "train")
        # 得到游标
        self.cursor = self.connect.cursor()
        print("成功连接到数据库")

    def close_spider(self,spider):
        #关闭游标和连接
        self.cursor.close()
        self.connect.close()
```
#反爬虫方法
1.模拟浏览器的头部信息
[User-Agent](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/User-Agent)
2.cookies验证

#scrapy 中间件
1.系统代理中间件
```
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 400,
}
```
作业2用request模拟登录显示CSRF需要继续尝试