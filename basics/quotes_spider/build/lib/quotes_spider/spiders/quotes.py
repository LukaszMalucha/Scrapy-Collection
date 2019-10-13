# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

from quotes_spider.items import QuotesSpiderItem


class QuotesSpider(scrapy.Spider):
	name = 'quotes'
	allowed_domains = ['quotes.toscrape.com']
	start_urls = ['http://quotes.toscrape.com/']

	def parse(self, response):

		
		quotes = response.xpath('//*[@class="quote"]')
		for quote in quotes:
			# define item loader from items.py
			l = ItemLoader(item=QuotesSpiderItem(), selector=quote)
			text = quote.xpath('.//*[@class="text"]/text()').extract_first() 
			author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
			tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()

			l.add_value('text',text)
			l.add_value('author', author)
			l.add_value('tags', tags)
			yield l.load_item()
			

		next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
		absoulte_next_page_url = response.urljoin(next_page_url)
		yield scrapy.Request(absoulte_next_page_url)	
