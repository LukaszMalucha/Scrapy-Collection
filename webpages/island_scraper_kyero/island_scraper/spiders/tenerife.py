# -*- coding: utf-8 -*-
import scrapy
from pathlib import Path
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from island_scraper.items import IslandScraperItem
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

# from pathlib import Path
# from selenium import webdriver
# from scrapy.selector import Selector

# driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")))
# driver.get("https://www.kyero.com/en/tenerife-apartments-for-sale-0l55570g1?max_price=120000&min_beds=2&min_property_size=40&page=5&sort=popularity_desc")
# sel = Selector(text=driver.page_source)


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


class TenerifeSpider(scrapy.Spider):
	name = 'tenerife'
	allowed_domains = ['www.kyero.com']
	start_urls = ['http://www.kyero.com/']

	def parse(self, response):
		agent = user_agent_rotator.get_random_user_agent()
		options.add_argument(f"user-agent={agent}")
		self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
		# self.driver = webdriver.Firefox(executable_path=str(Path(Path.cwd(), "geckodriver.exe")))
		self.driver.set_window_size(randrange(1100, 1200), randrange(800, 900))
		self.driver.get("https://www.kyero.com/en/tenerife-apartments-for-sale-0l55570g1?max_price=150000&min_beds=2&min_property_size=40&sort=popularity_desc/")
		sleep(2)
		body = self.driver.find_element_by_css_selector('body')
		body.send_keys(Keys.PAGE_DOWN)
		sleep(1)
		body.send_keys(Keys.PAGE_UP)
		sleep(1)
		body.send_keys(Keys.PAGE_DOWN)
		body.send_keys(Keys.HOME)

		sel = Selector(text=self.driver.page_source)

		pages = sel.xpath('.//span[@class="search-results__count"]/text()').extract()[0]
		pages = pages.split(" ")[0]
		pages = pages.replace(",", "")
		pages = int(pages) / 20 
		pages_count = int(pages) + 1
		sleep(1)
		self.driver.quit()

		for page in range (1):
			agent = user_agent_rotator.get_random_user_agent()
			options.add_argument(f"user-agent={agent}")
			self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
			self.driver.set_window_size(randrange(1100, 1200), randrange(800, 900))
			self.driver.get(f"https://www.kyero.com/en/tenerife-apartments-for-sale-0l55570g1?max_price=150000&min_beds=2&min_property_size=40&page={page}&sort=popularity_desc")
			sleep(1)
			body = self.driver.find_element_by_css_selector('body')
			sleep(1)
			body.send_keys(Keys.END)
			sleep(1)
			body.send_keys(Keys.HOME)	

			try:
				picture = self.driver.find_elements_by_css_selector('figure')[randrange(1, 5)]
				hov = ActionChains(driver).move_to_element(picture)
				hov.perform()
			except:
				pass

			sel = Selector(text=self.driver.page_source)	
			adverts = sel.xpath('//article[contains(@class, "bg-white")]')

			for advert in adverts:
				try:
					l = ItemLoader(item=IslandScraperItem(), selector=advert)
					title = advert.xpath('.//a[contains(@class, "inline-block hover-underline")]/text()').extract_first()
					link_string = advert.xpath('.//a[contains(@class, "inline-block hover-underline")]/@href').extract_first()
					link = "https://www.kyero.com" + link_string
					locality = title.split(" in ")[1]	
					details = advert.xpath('.//ul[contains(@class, "flex")]/li/span/text()')
					price_string = advert.xpath('.//span[contains(@class, "p-5")]/text()').extract_first()[1:]
					if price_string:
						price = price_string.split(" ")[1]
						price = price[1:]
						price = price.replace(",", "")				
					beds = advert.xpath('.//ul[contains(@class, "flex")]/li/span/text()').extract_first()
					size_string = advert.xpath('.//ul[@class="flex"]/li/span/text()')[-1].extract()
					size = size_string.split(" ")[0]
					date = datetime.today().strftime('%Y-%m-%d')

				except:
					pass	

				l.add_value('title', title)						
				l.add_value('island', "Tenerife")		
				l.add_value('locality', locality)
				l.add_value('price', price)
				l.add_value('beds', beds)
				l.add_value('size', size)
				l.add_value('link', link)	
				l.add_value('date', date)
				l.add_value('ad_type', "sale")
				yield l.load_item()		

			sleep(5)	
			self.driver.quit()		

		
