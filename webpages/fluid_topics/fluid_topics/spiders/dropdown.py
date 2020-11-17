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


## AVOID HANDSHAKE ERRORS
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')  
options.add_argument('--ignore-ssl-errors')

class DropdownSpider(scrapy.Spider):
	name = 'dropdown'
	allowed_domains = ['johnsoncontrols.fluidtopics.net']
	start_urls = ['https://johnsoncontrols.fluidtopics.net/search/all?period=custom_1896-01-01_1999-12-31&sort=last_update&content-lang=en-US']

	data_ranges = ['1896-01-01_1999-12-31','2000-01-01_2000-12-31','2001-01-01_2001-12-31', '2002-01-01_2002-12-31', '2003-01-01_2003-12-31', '2004-01-01_2004-12-31','2005-01-01_2005-12-31']

	# Year 2019 + has to be scraped monthly
	def parse(self, response):
		self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")),chrome_options=options)
		self.driver.get('https://johnsoncontrols.fluidtopics.net/search/all?query=North+American+Emissions+Compliance&period=custom_2018-01-01_2018-12-31&sort=last_update&content-lang=en-US')
		sleep(5)
		page = Selector(text = self.driver.page_source)



		sel = Selector(text = self.driver.page_source)	
		document_cards = sel.xpath('//*[contains(@class, "searchresult-new-component")]')
		
		for card in document_cards:		
			l = ItemLoader(item = FluidTopicsItem(), selector = card)	
			dropdown = card.xpath('.//*[@class="gwt-ListBox"]/option/text()').extract()	
			title = card.xpath('.//*[@class="searchresult-title"]/a/span/text()').extract_first()
			link = card.xpath('.//*[@class="searchresult-title"]/a/@href').extract_first()
			metadata = card.xpath('.//*[@class="metadata-list"]/li/@title').extract()
			l.add_value('title', title)
			l.add_value('dropdown', dropdown)
			l.add_value('link', link)
			l.add_value('metadata', metadata)
			yield l.load_item()