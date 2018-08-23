# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest


class GitscraperSpider(scrapy.Spider):
	name = 'gitscraper'
	allowed_domains = ['github.com']
	start_urls = ['https://github.com/login']

	def parse(self, response):
		yield FormRequest.from_response(
			response,
			url='https://github.com/session',
			formdata= {
			'login' : '****',
			'password': '****'},
			callback = self.parse_after_login)

	def parse_after_login(self, response):
		pass    
