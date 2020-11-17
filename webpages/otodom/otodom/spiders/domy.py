# -*- coding: utf-8 -*-
import scrapy
from apt.items import AptItem
from pathlib import Path
from random import randrange
from random_user_agent.params import SoftwareName, OperatingSystem
from random_user_agent.user_agent import UserAgent
from scrapy import Spider
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

## AVOID HANDSHAKE ERRORS
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--incognito")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")


software_names = [SoftwareName.FIREFOX.value]
operating_systems = [OperatingSystem.WINDOWS.value,] 
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)


class DomySpider(scrapy.Spider):
	name = 'domy'
	allowed_domains = ['otodom.pl']
	start_urls = ['http://otodom.pl/']

	   

	def parse(self, response):
		agent = user_agent_rotator.get_random_user_agent()
		options.add_argument(f"user-agent={agent}")
 



		"""
		OPEN SELENIUM WINDOW, GO TO THE PAGE, WAIT 2 SEC FOR PAGE RELOAD
		"""
		self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
		self.driver.set_window_size(randrange(1100, 1200), randrange(800, 900))
		self.driver.get('https://www.otodom.pl/sprzedaz/wroclaw/?search%5Bdescription%5D=1&search%5Bregion_id%5D=1&search%5Bsubregion_id%5D=381&search%5Bcity_id%5D=39&nrAdsPerPage=72')
		sleep(2)

		body = self.driver.find_element_by_css_selector('body')
		body.send_keys(Keys.PAGE_DOWN)
		sleep(1)
		body.send_keys(Keys.PAGE_UP)
		sleep(1)
		body.send_keys(Keys.PAGE_DOWN)
		body.send_keys(Keys.HOME)


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
			urls.append(f"https://www.otodom.pl/sprzedaz/wroclaw/?search%5Bdescription%5D=1&search%5Bregion_id%5D=1&search%5Bsubregion_id%5D=381&search%5Bcity_id%5D=39&nrAdsPerPage=72&page={item + 1}")

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










