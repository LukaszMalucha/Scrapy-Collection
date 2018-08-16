# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request, FormRequest


class EplanningSpider(Spider):
    name = 'eplanning'
    allowed_domains = ['eplanning.ie']
    start_urls = ['http://eplanning.ie/']

    def parse(self, response):
        ### Get county URLS
        urls = response.xpath('//a[contains(@href,"eplanning")]/@href').extract()
        for url in urls:   ## slice with [0:5] for test run
            yield Request(url, callback=self.parse_application)
         
        ### Get application url    
    def parse_application(self, response):
        app_url = response.xpath('//*[@class="glyphicon glyphicon-inbox btn-lg"]/following-sibling::a/@href').extract_first()
        yield Request(response.urljoin(app_url), callback=self.parse_form)
        
        ### get search form results (42 days)
    def parse_form(self, response):
        yield FormRequest.from_response(response, 
                                        formdata={'RdoTimeLimit': '42'},
                                        dont_filter=True,    ### filter duplicates
                                        formxpath='(//form)[2]', callback=self.parse_pages)        
        
        ### application pages
    def parse_pages(self, response):
        application_urls = response.xpath('//td/a/@href').extract()
        for url in application_urls:
            url = response.urljoin(url)
            yield Request(url, callback=self.parse_items)
        
        ### go to next page
        next_page_url = response.xpath('//*[@rel="next"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url, callback=self.parse_pages)
        
        ### application data
    def parse_items(self, response):
        agent_btn = response.xpath('//*[@value="Agents"]/@style').extract_first()
        if 'display: inline;  visibility: visible;' in agent_btn:
            name = response.xpath('//tr[th="Name :"]/td/text()').extract_first()
            address_first = response.xpath('//tr[th="Address :"]/td/text()').extract()
            address_second = response.xpath('//tr[th="Address :"]/following-sibling::tr/td/text()').extract()[0:3]
            address = address_first + address_second
            phone = response.xpath('//tr[th="Phone :"]/td/text()').extract_first()
            email = response.xpath('//tr[th="e-mail :"]/td/text()').extract_first()
            
            url = response.url
            
            yield  {'name': name, 'address': address, 'phone': phone, 'email': email, 'url':url}
            
        else:
            self.logger.info('Agent button not present')
        
        
    