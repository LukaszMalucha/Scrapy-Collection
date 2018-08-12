# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']                          ## change to login page 

    def parse(self, response):                      
            csrf_token = response.xpath('.//*[@name="csrf_token"]/@value').extract_first()  ### get the csrf token
            yield FormRequest('http://quotes.toscrape.com/login',
                                formdata={'csrf_token': csrf_token,
                                          'username': 'asd',
                                          'password': 'asd'},
                                callback=self.parse_after_login)
        
        
    def parse_after_login(self, response):
            open_in_browser(response)         ## verify if spider was sucessful

