# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FluidTopicsItem(scrapy.Item):
	title = scrapy.Field()
	# dropdown = scrapy.Field()
	link = scrapy.Field()
	metadata = scrapy.Field()
