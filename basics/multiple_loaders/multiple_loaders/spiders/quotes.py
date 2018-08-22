# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from train.items import TrainItem

class QuotesSpider(scrapy.Spider):
	name = 'quotes'
	allowed_domains = ['quotes.toscrape.com']
	start_urls = ['http://quotes.toscrape.com/']

	def parse(self, response):
		l = ItemLoader(item=TrainItem(), response = response)
		header = response.xpath('.//h1/a/text()').extract_first()
		tags = response.xpath('.//span[@class="tag-item"]/a/text()').extract()
		l.add_value('header', header)
		l.add_value('tags', tags)
		yield l.load_item()

		# scrape text of quote from every page, author, tags
		quotes = response.xpath('//*[@class="quote"]')
		for quote in quotes:
			l2 = ItemLoader(item=TrainItem(), response = response)
			quotes_text = quote.xpath('.//*[@class="text"]/text()').extract_first()
			author = quote.xpath('.//*[@class="author"]/text()').extract_first()
			quote_tags = quote.xpath('.//*[@class="tags"]/a/text()').extract_first()


			l2.add_value('quotes_text', quotes_text)
			l2.add_value('author', author)
			l2.add_value('quote_tags', quote_tags)
			yield l2.load_item()
		
			
		next_page_url = response.xpath('.//*[@class="next"]/a/@href').extract_first() 
		absolute_next_page_url = response.urljoin(next_page_url)   
		yield scrapy.Request(absolute_next_page_url)


