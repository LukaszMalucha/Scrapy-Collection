# -*- coding: utf-8 -*-
import selenium
from scrapy import Spider
from parsel import Selector
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.loader import ItemLoader
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from faang.items import FaangItem
import pandas as pd

## AVOID HANDSHAKE ERRORS
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')  
options.add_argument('--ignore-ssl-errors')




dataset = pd.read_csv('apple_links.csv')
dataset = dataset.dropna()
dataset = dataset.drop_duplicates()
link_urls = dataset['link'].values.tolist() 

# link_urls = [ 'https://www.linkedin.com/in/anita-hideg-09749b5b/','https://www.linkedin.com/in/eoinoshea/']

class CountriesSpider(Spider):
	name = 'countries'
	allowed_domains = ['www.linkedin.com']
	start_urls = ['http://www.linkedin.com/']

	def parse(self, response):
			
			self.driver = webdriver.Chrome('D:/PYTHON/WebScraping/chromedriver',chrome_options=options)  ## path to chromedriver on disk
			self.driver.get('https://linkedin.com/')   


			username = self.driver.find_element_by_class_name('login-email')
			username.send_keys('lucasmalucha@gmail.com')
			sleep(0.5)	

			password = self.driver.find_element_by_id('login-password')
			password.send_keys('Chujek2323')
			sleep(0.5)
			
			sign_in_button = self.driver.find_element_by_xpath('//*[@type="submit"]')
			sign_in_button.click()
			sleep(2)

			for element in link_urls:
				l = ItemLoader(item = FaangItem(), selector= element)
				self.driver.get(element)
				sel = Selector(text = self.driver.page_source)
				sleep(1)
				try:
					country = sel.xpath("normalize-space(.//h3/text())").extract_first()
					l.add_value('country', country)

				except:
					pass		

				yield l.load_item()	

			self.driver.quit()