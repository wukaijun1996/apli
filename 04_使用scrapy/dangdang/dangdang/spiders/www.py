import scrapy


class WwwSpider(scrapy.Spider):
    name = 'www'
    allowed_domains = ['https://www.baidu.com/']
    start_urls = ['http://https://www.baidu.com//']

    def parse(self, response):
        pass
