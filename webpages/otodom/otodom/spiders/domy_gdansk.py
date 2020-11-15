# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from apt.items import AptItem
from selenium.webdriver.common.keys import Keys
from time import sleep





class DomyPoznanSpider(scrapy.Spider):  # update class to DomyPoznan 
	name = 'domy_gdansk'          		#  if you use base of spider but want to scrape other page, you need to updatenem of the spider 
	allowed_domains = ['otodom.pl']
	start_urls = ['http://otodom.pl/']

	   

	def parse(self, response):

		"""
		OPEN SELENIUM WINDOW, GO TO THE PAGE, WAIT 2 SEC FOR PAGE RELOAD
		"""
		self.driver=webdriver.Chrome('D:/Panda_projects/Wroclaw/chromedriver')
		self.driver.get('https://www.otodom.pl/sprzedaz/gdansk/?search%5Bdescription%5D=1&search%5Bregion_id%5D=11&search%5Bsubregion_id%5D=439&search%5Bcity_id%5D=40&nrAdsPerPage=72')
		sleep(3)

		"""
		FIND BODY SECTION ON THE PAGE ADN CLICK END BUTTON TO GO TO THE BOTTOM OF THE PAGE
		LOAD SELENIUM WEBPAGE TO SCRAPY, FIND OUT NUMBER OF PAGES TO SCRAPE, 
		"""
		body=self.driver.find_element_by_css_selector("body")
		body.send_keys(Keys.END)
		sel = Selector(text =self.driver.page_source)
		number_of_pages = sel.xpath('//ul[contains(@class, "pager")]/li/a/text()')[-1].extract()

		""" 
		USE NUMBER OF PAGES TO SCRAPE TO CREATE A LIST OF URLS FOR THE ITERATION
		"""
		urls = []	
		for item in range(int(number_of_pages)):
			urls.append(f"https://www.otodom.pl/sprzedaz/gdansk/?search%5Bdescription%5D=1&search%5Bregion_id%5D=11&search%5Bsubregion_id%5D=439&search%5Bcity_id%5D=40&nrAdsPerPage=72&page={item + 1}")
			

		"""
		GO TO EACH PAGE FROM THE LIST ABOVE AND AND FIND ELEMENT THAT YOU ARE INTERESTED IN
		"""


		for element in urls:
			self.driver.get(element)
			sel = Selector(text =self.driver.page_source)
			content = sel.xpath('//div[@class="col-md-content section-listing__row-content"]')
			offers=content.xpath('.//div[@class="offer-item-details"]')
		
			for offer in offers:
				l=ItemLoader(item=AptItem(),selector= offer)
				url=offer.xpath('.//h3/a/@href').extract_first() 
				location=offer.xpath('.//p/text()').extract_first()

				details=offer.xpath('.//ul/li/text()').extract()
				if len(details)==4:
					number_rooms=offer.xpath('.//ul/li/text()').extract()[0]
					area=offer.xpath('.//ul/li/text()').extract()[2]
					price_per_meter=offer.xpath('.//ul/li/text()').extract()[3]



				l.add_value('url',url)
				l.add_value('location',location)
				l.add_value('number_rooms',number_rooms)
				l.add_value('area',area)
				l.add_value('price_per_meter',price_per_meter)
			
				yield l.load_item()










