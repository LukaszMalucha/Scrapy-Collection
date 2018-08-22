# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TrainItem(scrapy.Item):
	header = scrapy.Field()
	tags = scrapy.Field()
	quotes_text = scrapy.Field()
	author = scrapy.Field()
	quote_tags = scrapy.Field()

