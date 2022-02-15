#-*- codeing = utf-8 -*-
import scrapy


class WkjSpider(scrapy.Spider):
    # 爬虫文件的名字
    name = 'wkj'
    # 允许爬取的域名
    allowed_domains = ['http://www.dangdang.com/']
    start_urls = ['http://category.dangdang.com/cp01.03.42.00.00.00.html']

    # 爬虫命令之后要执行的函数
    def parse(self, response):
        print("晚上好 11人")
        print("============================================开始啦")

        name = []
        price = []
        for i in range(1,61):
            resp1 = response.xpath('//*[@class="line{}"]/p[1]/a/@title'.format(i))
            resp2 = response.xpath('//*[@class="line{}"]/p[3]/span[1]/text()'.format(i))
            name.append(resp1.extract()[0])
            price.append(resp2.extract()[0])
            # print(resp1.extract(),resp2.extract())
        print(name)
        print(price)


# //*[@id="p29361417"]/p[3]/span[1]

