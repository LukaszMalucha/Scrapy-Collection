# -*- coding: utf-8 -*-
import scrapy
import selenium
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.loader import ItemLoader
from otodom.items import OtodomItem
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class DomSpider(scrapy.Spider):
	name = 'dom'
	allowed_domains = ['www.otodom.pl']
	start_urls = ['https://www.otodom.pl/sprzedaz/mieszkanie/wroclaw/?dist=0&subregion_id=381&city_id=39&nrAdsPerPage=72&search%5Bpaidads_listing%5D=1']

	def start_requests(self):
		self.driver = webdriver.Chrome('D:/PYTHON/WebScraping/chromedriver')
		self.driver.get('https://www.otodom.pl/sprzedaz/mieszkanie/wroclaw/?dist=0&subregion_id=381&city_id=39&nrAdsPerPage=72&search%5Bpaidads_listing%5D=1')

		sel = Selector(text = self.driver.page_source)
		content = sel.xpath('//div[@class="col-md-content section-listing__row-content"]')
		offer_urls = content.xpath('.//*[@class="offer-item-details"]//a/@href').extract()
		for url in offer_urls:
			yield Request(url, callback= self.parse_details)
		while True:

			try:
				next_page = self.driver.find_element_by_xpath('.//li[@class="pager-next"]//a')
				sleep(2)                                                           
				self.logger.info('Wait 2 seconds')
				next_page.send_keys(selenium.webdriver.common.keys.Keys.ENTER)

				sel = Selector(text=self.driver.page_source)
				content = sel.xpath('//div[@class="col-md-content section-listing__row-content"]')
				offer_urls = content.xpath('.//*[@class="offer-item-details"]//a/@href').extract()
				for url in offer_urls:
					yield Request(url, callback= self.parse_details)


			except NoSuchElementException:   					   
				self.logger.info('Last Page')
				self.driver.quit()
				break		

	def parse_details(self, response):
		url = response.url
		yield {'url': url}
