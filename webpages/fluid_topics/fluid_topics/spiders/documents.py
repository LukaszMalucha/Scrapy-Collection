# -*- coding: utf-8 -*-
import scrapy
import selenium
from pathlib import Path
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.loader import ItemLoader
from fluid_topics.items import FluidTopicsItem
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep

# Helper function to create dates list:

def create_date_list():
	date_list = []
	date_list.append('1896-01-01_1999-12-31')  
	for i in range(0,10):    
		date_list.append(f'200{i}-01-01_200{i}-12-31') 
	for i in range(10,19):       
		date_list.append(f'20{i}-01-01_20{i}-12-31')
	return date_list

# Helper function to create a list of dates for 2019
def create_annual_list():
	annual_list = []
	for i in range(1,10):    
		annual_list.append(f'2019-0{i}-01_2019-0{i}-31')
	for i in range(10,13):    
		annual_list.append(f'2019-{i}-01_2019-{i}-31')  		
	return annual_list		


## AVOID HANDSHAKE ERRORS
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')  
options.add_argument('--ignore-ssl-errors')



class DocumentsSpider(scrapy.Spider):
	name = 'documents'
	allowed_domains = ['johnsoncontrols.fluidtopics.net']
	start_urls = ['https://johnsoncontrols.fluidtopics.net/search/all?period=custom_1896-01-01_1999-12-31&sort=last_update&content-lang=en-US']

	date_list = (create_date_list())
	annual_list = (create_annual_list())

	# Year 2019 + has to be scraped monthly
	def parse(self, response):
		self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")),chrome_options=options)
		# SWTICH FOR self.annual_list for 2019
		for date in self.date_list:			
			self.driver.get(f'https://johnsoncontrols.fluidtopics.net/search/all?period=custom_{date}&sort=last_update&content-lang=en-US')
			sleep(8)
			page = Selector(text = self.driver.page_source)
			
			document_count = page.xpath('//*[@class="info-results-count"]/@data-results-count').extract_first()	
			page_loads = int(int(document_count) / 20) + 1
			for i in range(page_loads):
				body = self.driver.find_element_by_css_selector('body')
				body.send_keys(Keys.END)
				# sleep(1)
				try:
					button = self.driver.find_element_by_xpath('//button[contains(@class, "searchpager-load-more-button")]')	
					button.click()
				except:
					pass		
				sleep(1)

			sel = Selector(text = self.driver.page_source)	
			document_cards = sel.xpath('//*[contains(@class, "searchresult-new-component")]')
			
			for card in document_cards:		
				l = ItemLoader(item = FluidTopicsItem(), selector = card)	
				title = card.xpath('.//*[@class="searchresult-title"]/a/span/text()').extract_first()
				# dropdown = card.xpath('.//*[@class="gwt-ListBox"]/option/text()').extract()
				link = card.xpath('.//*[@class="searchresult-title"]/a/@href').extract_first()
				metadata = card.xpath('.//*[@class="metadata-list"]/li/@title').extract()
				l.add_value('title', title)
				# l.add_value('dropdown', dropdown)
				l.add_value('link', link)
				l.add_value('metadata', metadata)
				yield l.load_item()

		
			