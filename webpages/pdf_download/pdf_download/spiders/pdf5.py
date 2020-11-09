# -*- coding: utf-8 -*-
import scrapy
from pathlib import Path
from selenium import webdriver
from scrapy.selector import Selector
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import csv
from random import randrange

# prepare a list of links
my_list = []
with open(Path(Path.cwd(), "pdfs.csv"), 'r') as my_file:
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
options.add_experimental_option('prefs',  {
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
    }
)

class PdfSpider(scrapy.Spider):
    name = 'pdf5'
    allowed_domains = ['johnsoncontrols.com']
    start_urls = ['http://johnsoncontrols.com/']

    def parse(self, response):
        self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
        self.driver.set_window_size(randrange(1860, 1920), randrange(800, 900))
        for url in pdf_urls[4000:]:
        	self.driver.get(url)
        	sleep(1)
