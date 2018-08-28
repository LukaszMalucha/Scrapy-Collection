# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OtodomItem(scrapy.Item):
	price = scrapy.Field()
	price_per_m = scrapy.Field()
	area = scrapy.Field()
	rooms = scrapy.Field()
	level = scrapy.Field()
