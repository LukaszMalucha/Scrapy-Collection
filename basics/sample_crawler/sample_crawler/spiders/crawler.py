# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlerSpider(CrawlSpider):                                              ## Swap to Crawl
    name = 'crawler'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']                                ## remove www to avoid twisted.internet.error


    rules = (Rule(LinkExtractor(deny_domains=('google.com')), callback='parse_page', follow=False),)
    ## additional LinkExtractor arguments deny_domains=('google.com'), allow = ('music')
    def parse_page(self, response):
        yield {'URL': response.url}
