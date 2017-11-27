# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from books.item import BookItem

class HomeSpider(CrawlSpider):
    name = 'home'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    rules = (Rule(LinkExtractor(allow=(), restrict_css=('.next',)),
             callback="parse_page",
             follow=True),)

    def parse_page(self, response):
        items = []
        books = response.xpath('//ol/li/article')
        index = 0
        for book in books:
            item = BookItem()
            title = books.xpath('//h3/a/text()')[index].extract()
            item['title'] = str(title).encode('utf-8').strip()
            price = books.xpath('//article/div[contains(@class, "product_price")]/p[1]/text()')[index].extract()
            item['price'] = str(price).encode('utf-8').strip()
            items.append(item)
            index += 1
            yield item           
