# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DaftcrawlerItem(scrapy.Item):
	name = scrapy.Field()
	price = scrapy.Field()
	property_type = scrapy.Field()
	beds = scrapy.Field()
	bath = scrapy.Field()
	features = scrapy.Field()
	address = scrapy.Field()
	url = scrapy.Field()