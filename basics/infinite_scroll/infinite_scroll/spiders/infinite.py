# -*- coding: utf-8 -*-
import scrapy
import json


class InfiniteSpider(scrapy.Spider):
    name = 'infinite'
    allowed_domains = ['quotes.toscrape.com']
    api_url = 'http://quotes.toscrape.com/api/quotes?page={}'
    start_urls = ['http://quotes.toscrape.com/api/quotes?page=1']

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data['quotes']:
        	yield {
        		'author_name': quote['author']['name'],
        		'text': quote['text'],
        		'tag': quote['tags']
        	}
        if data['has_next']:
        	next_page = data['page'] + 1
        	yield scrapy.Request(url=self.api_url.format(next_page), callback=self.parse)
        		