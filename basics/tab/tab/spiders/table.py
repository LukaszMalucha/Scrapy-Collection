# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from tab.items import TabItem


class TableSpider(scrapy.Spider):
	name = 'table'
	allowed_domains = ['en.wikipedia.org']
	start_urls = ['https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population']

	def parse(self, response):
		table =  response.xpath('//table[@class="wikitable sortable"]')[0]
		table_rows = table.xpath('.//tr')[1:]
		

		for row in table_rows:
			l = ItemLoader(item=TabItem(), selector=row)
			rank = row.xpath('normalize-space(.//td/text())').extract_first()
			city = row.xpath('normalize-space(.//td[2]//text())').extract_first()
			l.add_value('rank', rank)
			l.add_value('city', city)
			yield l.load_item() 

