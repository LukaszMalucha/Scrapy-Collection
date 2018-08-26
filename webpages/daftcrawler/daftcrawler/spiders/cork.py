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
		self.driver.get('https://www.daft.ie/cork-city/residential-property-for-rent/')

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
				for url in property_urls:
					 yield Request(url, meta= {'url': url}, callback= self.parse_details)

			except NoSuchElementException:   					   
				self.logger.info('Last Page')
				self.driver.quit()
				break	


	def parse_details(self, response):
		l = ItemLoader(item=DaftcrawlerItem(), response=response)
		url = response.meta['url']
		name = response.xpath('normalize-space(.//div[@class="smi-object-header"]/h1/text())').extract_first() 

		price_string = response.xpath('//*[@id="smi-price-string"]/text()').extract_first()
		price = price_string.split(' Per ')[0]
		price = price[1:]
		unit = price_string.split(' Per ')[1]
		if unit == "week":
			price = int(int(price) * 4.5)
			l.add_value('price', price)
		else:
			price = price
			l.add_value('price', price)
			

		property_type = response.xpath('//*[@class="header_text"]/text()').extract_first()
		property_type = property_type.split(' to ')[0] 

		try:
			beds = response.xpath('//*[@class="header_text"]/text()').extract()[1]
			beds = beds.split(' ')[0]
			bath = response.xpath('//*[@class="header_text"]/text()').extract()[2]
			bath = bath.split(' ')[0]
			l.add_value('beds', beds)
			l.add_value('bath', bath)

		except:
			pass	

		facilities_list = response.xpath('.//tbody/tr/td/ul/li/text()').extract()
		facilities_list = response.xpath('//*[@valign="top"]')
		features = facilities_list.xpath('.//li/text()').extract()
		address = response.xpath('//*[@class="map_info_box"]/text()').extract()[0]


		l.add_value('name', name)
		l.add_value('property_type', property_type)
		l.add_value('features', features)
		l.add_value('address', address)
		l.add_value('url', url)
		return l.load_item()  

