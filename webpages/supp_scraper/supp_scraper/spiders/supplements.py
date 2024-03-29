# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class SupplementsSpider(scrapy.Spider):
    name = 'supplements'
    allowed_domains = ['www.discountsupplements.ie']
    start_urls = ['https://discountsupplements.ie/index.php?route=product/brands']

    def parse(self, response):
        company_urls = response.xpath('//*[@class="md-25 xl-25"]/a/@href').extract()
        for url in company_urls: 
            url = url + '#/sort=p.sort_order/order=ASC/limit=100 #/sort=p.sort_order/order=ASC/limit=1000'
            yield Request(url, callback=self.parse_products)
            
    def parse_products(self, response):
        products = response.xpath('//*[@class="name"]/a/@href').extract()
        brand = response.xpath('//*[@itemprop="title"]/text()').extract()[2]      
        for product in products:            
            yield Request(product, 
                          callback=self.parse_details, 
                          meta={'brand': brand})

            
    def parse_details(self, response):
        brand = response.meta['brand']
        name = response.xpath('//h1/text()').extract_first()
        price = response.xpath('//*[@class="product-price"]/text()').extract_first()
        reviews_count = response.xpath('//*[@class="active"]/a/text()')[1].extract()
        reviews_count = reviews_count[9:10]
        reviews_count = reviews_count.split(')')[0]
        yield {'name': name,
               'brand': brand,
               'price': price,
               'reviews_count': reviews_count}