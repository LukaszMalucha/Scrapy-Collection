# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.loader import ItemLoader
from house.items import HouseItem




class BallincolligSpider(scrapy.Spider):
    name = 'ballincollig'
    allowed_domains = ['propertypriceregisterireland.com']
    start_urls = ['http://propertypriceregisterireland.com/']

    def parse(self, response):
        for page in range(1,11):
            url = f"https://propertypriceregisterireland.com/search/area/ballincollig/&page={str(page)}/"
            yield Request(url, callback=self.parse_homes)



    def parse_homes(self, response):     

        rows = response.xpath('//tr[contains(@class,"inre-clm")]')
        for row in rows:


            date = row.xpath(".//td/text()")[0].extract()
            address_number = row.xpath('.//div[contains(@class,"address")]/text()')[0].extract()
            address_area_1 = row.xpath('.//div[contains(@class,"address")]/a/text()')[0].extract()
            try:
                address_area_2 = row.xpath('.//div[contains(@class,"address")]/text()')[1].extract()
            except:
                address_area_2 = ""    

            price = row.xpath(".//td/text()")[-2].extract()
            property_type = row.xpath(".//td/text()")[-1].extract()

            l = ItemLoader(item=HouseItem(), selector=row)

            l.add_value('date', date)    
            l.add_value('address_number', address_number)  
            l.add_value('address_area_1', address_area_1)   
            l.add_value('address_area_2', address_area_2) 
            l.add_value('price', price) 
            l.add_value('property_type', property_type) 

            yield l.load_item() 



