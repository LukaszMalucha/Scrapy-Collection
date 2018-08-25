# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request



class MultispiderSpider(scrapy.Spider):
	name = 'multispider'
	allowed_domains = ['books.toscrape.com', 'quotes.toscrape.com']
	start_urls = ['http://books.toscrape.com/', 'http://quotes.toscrape.com/' ]

	def parse(self, response):
		if "books.toscrape.com" in response.url:
			links = response.xpath('//h3/a/@href').extract()
			links = [response.urljoin(link) for link in links]

		elif "quotes.toscrape.com" in response.url:	
			links = response.xpath('//span/a[contains(@href,"author")]/@href').extract()
			links = [response.urljoin(link) for link in links]

		for link in links:
			yield Request(link, callback=self.parse_details)	



	def parse_details(self, response):
		url = response.url

		if "books.toscrape.com" in response.url:
			title = response.xpath('//h1/text()').extract()

			yield {'title' : title}

		elif "quotes.toscrape.com" in response.url:
			title = response.xpath('normalize-space(//h3/text())').extract_first()

			yield {'title' : title}




				


