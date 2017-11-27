# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider


class HomeSpider2(CrawlSpider):
    name = 'home2'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    rules = (Rule(LinkExtractor(allow=(), restrict_css=('.next',)),
             callback="parse_page",
             follow=True),)

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse_page(self, response):
        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
        for link in links:
            is_allowed = False
            for allowed_domain in self.allowed_domains:
                if allowed_domain in link.url:
                    is_allowed = True
            if is_allowed:
                print (link.url)
