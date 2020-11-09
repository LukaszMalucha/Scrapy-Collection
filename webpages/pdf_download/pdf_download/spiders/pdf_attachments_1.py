# -*- coding: utf-8 -*-
import scrapy
from pathlib import Path
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from pdf_download.items import PdfDownloadItem
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import csv
from random import randrange


# prepare a list of links
my_list = []
with open(Path(Path.cwd(), "maps.csv"), 'r') as my_file:
	reader = csv.reader(my_file, delimiter='\t')
	next(reader)
	
	my_list = list(reader)
	
html_urls = []
for sublist in my_list:
	for item in sublist:
		html_urls.append(item)

## TIMEOUT PARAMETER
timeout = 10

## AVOID HANDSHAKE ERRORS
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('prefs',  {
	"download.prompt_for_download": False,
	"download.directory_upgrade": True,
	"plugins.always_open_pdf_externally": True
	}
)

class PdfAttachmentsSpider(scrapy.Spider):
	name = 'pdf_attachments_1'
	allowed_domains = ['johnsoncontrols.com']
	start_urls = ['http://johnsoncontrols.com/']

	def parse(self, response):
		self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
		self.driver.set_window_size(randrange(1860, 1920), randrange(800, 900))
		for url in html_urls:
			l = ItemLoader(item=PdfDownloadItem(), selector=url)
			self.driver.get(url)
			sleep(2)
			sel = Selector(text=self.driver.page_source)
			try:
				attachment_button =  self.driver.find_element_by_xpath('//button[contains(@class, "fluid-aside-tab-id-mapattachments")]')
				attachment_button.click()
				sleep(1)
				page = Selector(text=self.driver.page_source)
				link_string = page.xpath('//a[contains(@class, "mapattachments-download-link")]/@href').extract_first()
				link = "https://johnsoncontrols.fluidtopics.net" + link_string
				link = link
			except:
				link = "FAILED"
				pass


			l.add_value('title', url)
			l.add_value('link', link)
			yield l.load_item()	

		self.driver.close()	