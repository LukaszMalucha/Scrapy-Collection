# -*- coding: utf-8 -*-

from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector                                           ## gathering urls 
from scrapy.http import Request
from selenium.common.exceptions import NoSuchElementException                  ## end of a loop 
from time import sleep
### SELECTORS:
#driver = webdriver.Firefox(executable_path="C:\\Program Files\\Mozilla Firefox\\firefox")
#driver = webdriver.Chrome('C:/chromedriver')


class SeleniumSpider(Spider):                                              
    name = 'selenium_crawler'
    allowed_domains = ['books.toscrape.com']
    
    
    def start_requests(self):
            self.driver = webdriver.Chrome('C:/chromedriver')                  ## init Chrome webdriver         
            self.driver.get('http://books.toscrape.com/')                      ## get into url
            
            sel = Selector(text=self.driver.page_source)                       ## def selector
            books = sel.xpath('//h3/a/@href').extract()                        ## get book page links
            for book in books:
                    url = 'http://books.toscrape.com/' + book                  ## modify scraped link
                    yield Request(url, callback= self.parse_book)
                    
            while True:                                                        ## try/except loop
                    try:
                            next_page = self.driver.find_element_by_xpath('//a[text()="next"]')  ## next page click
                            sleep(3)                                                             ## sleep 3s
                            self.logger.info('Wait 3 seconds')
                            next_page.click()
                            
                            sel = Selector(text=self.driver.page_source)       
                            books = sel.xpath('//h3/a/@href').extract()
                            for book in books:
                                    url = 'http://books.toscrape.com/catalogue/' + book            
                                    yield Request(url, callback= self.parse_book)
                                    
                    except NoSuchElementException:                             ## hit the last page
                            self.logger.info('Last Page')
                            self.driver.quit()
                            break
                    
    def parse_book(self, response):
            pass                  

