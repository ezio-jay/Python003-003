import scrapy
from spiders.items import SpidersItem
from scrapy.selector import Selector

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/films?showType=3&sortId=1/']

    #解析函数
    def parse(self, response):
        movie_list = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
        i = 0
        for movie in movie_list:
            if i > 9:
                break
            item = SpidersItem()
            movie_name = movie.xpath('./a/text()').get()
            movie_link = 'http://maoyan.com' + movie.xpath('./a/@href').get()
            item['movie_name'] = movie_name
            item['movie_link'] = movie_link
            i = i+1
            yield scrapy.Request(url=movie_link, meta={'item': item}, callback=self.parse2)
    #解析具体页面
    def parse2(self, response):
        item = response.meta['item']
        movie_types = Selector(response=response).xpath('//li[@class="ellipsis"]/a[@class="text-link"]/text()').getall()
        movie_type = ""
        for movie in movie_types:
            movie_type = movie_type + movie.strip() +" "
        movie_time = Selector(response=response).xpath('//li[@class="ellipsis"][last()]/text()').get()
        item['movie_type'] = movie_type
        item['movie_time'] = movie_time
        yield item