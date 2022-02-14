import scrapy


class DangwkjSpider(scrapy.Spider):
    name = 'dangwkj'
    allowed_domains = ['http://book.dangdang.com/?_utm_brand_id=11106']
    start_urls = ['http://http://book.dangdang.com/?_utm_brand_id=11106/']

    def parse(self, response):
        pass
