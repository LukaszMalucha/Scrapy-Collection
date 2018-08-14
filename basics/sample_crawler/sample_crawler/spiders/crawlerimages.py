# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
from scrapy.loader import ItemLoader
from sample_crawler.items import ImagesCrawlerItem




class CralwerimagesSpider(Spider):
    name = 'crawlerimages'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']



    def parse(self, response):
        books = response.xpath('//h3/a/@href').extract()
        for book in books:
            absolute_url = response.urljoin(book)
            yield Request(absolute_url, callback=self.parse_book)

        # process next page
        next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)

    def parse_book(self, response):
        l = ItemLoader(item=ImagesCrawlerItem(), response=response)    
        title = response.css('h1::text').extract_first()
        title = title.replace(':', ' ')                                        ## avoid windows error                                                                                                     
        price = response.xpath('//*[@class="price_color"]/text()').extract_first()

        image_urls = response.xpath('//img/@src').extract_first()
        image_urls = image_urls.replace('../..', 'http://books.toscrape.com/')
        ## rename img with pipelines.py
        l.add_value('title', title)
        l.add_value('price', price)
        l.add_value('image_urls', image_urls)
        
        return l.load_item()
        
