# -*- coding: utf-8 -*-
import scrapy
from pathlib import Path
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from dsc.items import DscItem
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import csv
from random import randrange
from datetime import datetime
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

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


class ProductsSpider(scrapy.Spider):
	name = 'products'
	allowed_domains = ['www.dsc.com']
	start_urls = ['http://www.dsc.com/']

	def parse(self, response):
		agent = user_agent_rotator.get_random_user_agent()
		options.add_argument(f"user-agent={agent}")
		self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
		self.driver.set_window_size(randrange(1100, 1200), randrange(800, 900))
		self.driver.get("https://www.dsc.com/index.php?n=products&filter=1,2,3,4,5,6,7")
		sleep(2)
		body = self.driver.find_element_by_css_selector('body')
		body.send_keys(Keys.PAGE_DOWN)
		sleep(1)
		body.send_keys(Keys.PAGE_UP)
		sleep(1)
		body.send_keys(Keys.PAGE_DOWN)
		body.send_keys(Keys.HOME)

		sel = Selector(text=self.driver.page_source)	


		products = sel.xpath('//div[contains(@class, "product-list-item")]')

		link_list = []

		for product in products:
			link_string = product.xpath('.//div[contains(@class, "list-title")]/a/@href').extract_first()
			product_link = "https://www.dsc.com/" + link_string
			link_list.append(product_link)

		for link in link_list[50:]:

			self.driver.get(link)
			sleep(1)
			sel = Selector(text=self.driver.page_source)	
			l = ItemLoader(item=DscItem(), selector=sel)		
			product_name = sel.xpath('//h1/text()').extract_first()	
			product_code = sel.xpath('//h3/text()').extract_first()
			# product_features = sel.xpath('.//ul[contains(@class, "product-features")]')
			# description = product_features.xpath('.//li/text()').extract()
			description = sel.xpath('.//div[contains(@class, "product-description")]/ul/li/text()').extract()
			main_image = sel.xpath('.//*[@class="link-product-image"]/@href').extract()
			images = sel.xpath('.//*[@class="link-product-image thumbnail "]/@href').extract()

			videos = sel.xpath('//iframe/@src').extract()
			document_accordion = sel.xpath('//h5/text()')
			document_list = []
			h5_buttons = self.driver.find_elements_by_xpath('//h5[contains(@class, "ui-accordion-header ui-helper-reset ui-state-default ui-corner-all")]')
			for h5_button in h5_buttons:
				try:
					h5_button_title = h5_button.text
					h5_button.click()
					sleep(0.5)
					h6_buttons = self.driver.find_elements_by_xpath('.//div[contains(@class, "accordion-2 ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom ui-accordion ui-widget ui-accordion-icons ui-accordion-content-active")]/h6')
					for h6_button in h6_buttons:
						h6_button_title = h6_button.text
						h6_button.click()
						sleep(0.5)
						sel = Selector(text=self.driver.page_source)
						documents = sel.xpath('.//div[contains(@class, "documents ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom ui-accordion-content-active")]/a')						
						for doc in documents:			
							document_title = doc.xpath('text()').extract_first()
							document_link = doc.xpath('@href').extract_first()
							document_list.append([h5_button_title, h6_button_title, document_title, document_link])
				except:
					pass			


			l.add_value('product_name', product_name)			
			l.add_value('product_code', product_code)
			l.add_value('description', description)
			l.add_value('main_image', main_image)
			l.add_value('images', images)
			l.add_value('videos', videos)
			l.add_value('document_list', document_list)
			l.add_value('website', link)
			yield l.load_item()			



# h5_buttons = driver.find_elements_by_xpath('//h5[contains(@class, "ui-accordion-header ui-helper-reset ui-state-default ui-corner-all")]')							
# h6_buttons = driver.find_elements_by_xpath('.//h6[contains(@class, "ui-accordion-header ui-helper-reset ui-state-default ui-corner-all")]')
# h6_buttons = driver.find_elements_by_xpath('.//div[contains(@class, "accordion-2 ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom ui-accordion ui-widget ui-accordion-icons ui-accordion-content-active")]/h6')
# sel = Selector(text=driver.page_source)
# documents = sel.xpath('.//div[contains(@class, "documents ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom ui-accordion-content-active")]/a')	

# document_links = sel.xpath('.//a')



# driver.get("https://www.dsc.com/index.php?n=products&o=view&id=2690")









