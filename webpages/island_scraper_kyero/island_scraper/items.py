# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IslandScraperItem(scrapy.Item):
	title = scrapy.Field()
	island = scrapy.Field()
	locality = scrapy.Field()
	price = scrapy.Field()
	beds = scrapy.Field()
	size = scrapy.Field()
	link = scrapy.Field()
	date = scrapy.Field()
	ad_type = scrapy.Field()