# -*- coding: utf-8 -*-
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.loader import ItemLoader
from daftcrawler.items import DaftcrawlerItem
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class CorkSpider(Spider):
	name = 'cork'
	allowed_domains = ['www.daft.ie']
	start_urls = ['http://www.daft.ie/']

	def parse(self, response):
		self.driver = webdriver.Chrome('D:/PYTHON/WebScraping/chromedriver')
		self.driver.get('https://www.daft.ie/cork/residential-property-for-rent/')

		sel = Selector(text = self.driver.page_source)
		property_urls = sel.xpath('.//*[@class="search_result_title_box"]/h2/a/@href').extract()
		property_urls = ['https://www.daft.ie' + property_url for property_url in property_urls]

		while True:

			try:
				next_page = self.driver.find_element_by_xpath('//li[@class="next_page"]/a')
				sleep(1)                                                           
				self.logger.info('Wait 2 seconds')
				next_page.click()

				sel = Selector(text=self.driver.page_source)
				property_urls = sel.xpath('.//*[@class="search_result_title_box"]/h2/a/@href').extract()
				property_urls = ['https://www.daft.ie' + property_url for property_url in property_urls] 

			except NoSuchElementException:   					   
				self.logger.info('Last Page')
				self.driver.quit()
				break	


	def parse_details(self, response):
		l = ItemLoader(item=DaftcrawlerItem(), response=response)
		name = response.xpath('normalize-space(.//div[@class="smi-object-header"]/h1/text())').extract_first() 


		l.add_value('name', name)
		return l.load_item()  