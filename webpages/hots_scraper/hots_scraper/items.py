# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HotsScraperItem(scrapy.Item):
    name = scrapy.Field()
    role = scrapy.Field()
    universum = scrapy.Field()
    abilities = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    
