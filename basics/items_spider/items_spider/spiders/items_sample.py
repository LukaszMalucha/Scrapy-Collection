# -*- coding: utf-8 -*-
import scrapy
from items_spider.items import ItemsSpiderItem


class ItemsSampleSpider(scrapy.Spider):
    name = 'items_sample'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        author = response.xpath('//*[@itemprop="author"]/text()').extract()
        
        item = ItemsSpiderItem()
        item['author'] = author
        return item