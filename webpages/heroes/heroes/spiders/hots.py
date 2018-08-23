# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request


class HotsSpider(scrapy.Spider):
	name = 'hots'
	allowed_domains = ['heroesofthestorm.com']
	start_urls = ['http://heroesofthestorm.com/']

	def start_requests(self):
		self.driver = webdriver.Chrome('D:/PYTHON/WebScraping/chromedriver')
		self.driver.get('https://heroesofthestorm.com/en-us/heroes/#/')

		sel = Selector(text = self.driver.page_source)
		heroes = sel.xpath('//*[@class="hero-link"]/@href').extract()
		for hero in heroes:
			url = 'https://heroesofthestorm.com/en-us/heroes/' + hero
			print (url)


	def parse_details(self, response):
		pass

