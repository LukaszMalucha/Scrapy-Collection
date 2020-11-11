# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DscItem(scrapy.Item):
	product_name = scrapy.Field()	
	product_code = scrapy.Field()
	description = scrapy.Field()
	main_image = scrapy.Field()
	images = scrapy.Field()
	videos = scrapy.Field()
	document_list = scrapy.Field()
	website = scrapy.Field()