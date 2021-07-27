# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseItem(scrapy.Item):

    date = scrapy.Field()
    address_number = scrapy.Field() 
    address_area_1 = scrapy.Field()   
    address_area_2 = scrapy.Field() 
    property_type = scrapy.Field()
    price = scrapy.Field() 

class BallincolligItem(scrapy.Item):

    price = scrapy.Field()
    address = scrapy.Field() 
    beds = scrapy.Field()   
    baths = scrapy.Field() 
    link = scrapy.Field()
    property_type = scrapy.Field() 
    popularity = scrapy.Field()
    date = scrapy.Field()
    size = scrapy.Field()
