# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.loader import ItemLoader




class JewelsSpider(Spider):


	def parse(self, response):
		urls = ('https://www.kilkennyshop.com/default/brand/?p={}'.format(i) for i in range(1,2)) #29
		for url in urls:
			yield Request(url, callback=self.parse_links)



	def parse_links(self, response):
		links = response.xpath('//*[@class="zoo-product-image"]/a/@href').extract()
		for link in links:
			try:
				yield Request(link, meta={'link': link }, callback=self.parse_details)
			except:
				pass	


	def parse_details(self, response):
		link = response.meta['link']
		name = response.xpath('//*[@class="base"]/text()').extract_first()
		price = response.xpath('//*[@class="price"]/text()').extract_first()
		descr = response.xpath('//*[@class="value"]/text()').extract_first()
		print(name, price, descr)
					


			

