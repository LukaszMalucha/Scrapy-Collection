# -*- coding: utf-8 -*-
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.loader import ItemLoader
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class JobsSpider(Spider):
	name = 'jobs'
	allowed_domains = ['www.irishjobs.ie']
	start_urls = ['https://irishjobs.ie/ShowResults.aspx?Keywords=python&autosuggestEndpoint=%2fautosuggest&Location=0&Category=&Recruiter=Company%2cAgency&btnSubmit=+&PerPage=232']

	def parse(self, response):
		self.driver = webdriver.Chrome('D:/PYTHON/WebScraping/chromedriver')
		self.driver.get('https://www.irishjobs.ie/ShowResults.aspx?Keywords=python&autosuggestEndpoint=%2fautosuggest&Location=0&Category=&Recruiter=Company%2cAgency&btnSubmit=+&PerPage=232')
		sel = Selector(text = self.driver.page_source)

		listings = sel.xpath('//div[@class="module job-result  "]')
		
		for listing in listings:

			job_title = listing.xpath('.//h2/a/text()').extract_first()
			location = listing.xpath('.//li[@class="location"]/a/text()').extract_first()
			salary = listing.xpath('.//li[@class="salary"]/text()').extract_first()
			company = listing.xpath('.//a[@itemprop="hiringOrganization"]/text()').extract_first()
			date = listing.xpath('.//li[@class="updated-time"]/text()').extract_first()
			date = date.split('Updated ')[1]
			url = listing.xpath('.//h2/a/@href').extract_first()
			url = "https://www.irishjobs.ie" + url

			yield {'job_title': job_title, 
					'location': location,
					'salary': salary,
					'company': company,
					'date': date,
					'url': url}

