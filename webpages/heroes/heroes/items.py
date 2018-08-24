# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HeroesItem(scrapy.Item):
	name = scrapy.Field()
	title = scrapy.Field()
	hero_class = scrapy.Field()
	description = scrapy.Field()
	stats = scrapy.Field()
	skillset = scrapy.Field()
	universum = scrapy.Field()

	image_urls = scrapy.Field()
	images = scrapy.Field()



