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
with open(Path(Path.cwd(), "pdf_links.csv"), 'r') as my_file:
	reader = csv.reader(my_file, delimiter='\t')
	next(reader)
	
	my_list = list(reader)
	
pdf_urls = []
for sublist in my_list:
	for item in sublist:
		pdf_urls.append(item)

## TIMEOUT PARAMETER
timeout = 10

## AVOID HANDSHAKE ERRORS
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

class PdfNamesSpider(scrapy.Spider):
	name = 'pdf_names5'
	allowed_domains = ['johnsoncontrols.fluidtopics.net']
	start_urls = ['http://johnsoncontrols.fluidtopics.net/']

	def parse(self, response):
		self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
		self.driver.set_window_size(randrange(1860, 1920), randrange(800, 900))
		for url in pdf_urls[4000:]:
			l = ItemLoader(item=PdfDownloadItem(), selector=url)
			self.driver.get(url)
			sleep(2)			
			sel = Selector(text=self.driver.page_source)
			try:		
				title = sel.xpath('//*[@class="vieweractionsbar-filename"]/@title').extract_first()
				link = url		
			except:
				title = "FAILED"
				link = url
				pass				
		
			l.add_value('title', title)
			l.add_value('link', link)
			yield l.load_item()