# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SampleCrawlerItem(scrapy.Item):

    pass


class ImagesCrawlerItem(scrapy.Item):
        title = scrapy.Field()
        price = scrapy.Field()
        
        image_urls = scrapy.Field()
        images = scrapy.Field()
        ## Modify settings.py as well