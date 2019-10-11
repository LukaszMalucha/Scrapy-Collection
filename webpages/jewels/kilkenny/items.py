# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KilkennyItem(scrapy.Item):
	product_id = scrapy.Field()
	name = scrapy.Field()
	price_euro = scrapy.Field()
	descr_1 = scrapy.Field()
	descr_2 = scrapy.Field()
	descr_3 = scrapy.Field()
	image_urls = scrapy.Field()
	images = scrapy.Field()
