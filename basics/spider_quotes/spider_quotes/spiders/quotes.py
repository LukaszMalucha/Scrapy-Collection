# -*- coding: utf-8 -*-
import scrapy



class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):                                                 ## assign selectors

        
        quotes = response.xpath('//*[@class="quote"]')                         ## Isolate quote container         
        for quote in quotes:
                text = quote.xpath('.//*[@class="text"]/text()').extract_first()           ### remember about dot! 
                author = quote.xpath('.//*[@class="author"]/text()').extract_first()
                tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()  ### select content from meta
                # tags = qutoe.xpath('.//*[@class="tag"]/text()').extract()    ### alternatively
                
                yield {'Quote':text, 'Author':author, 'Tags':tags}
                
                # scrapy crawl quotes -o items.csv
                
        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()       
        absolute_next_page_url = response.urljoin(next_page_url)              ## adding absolute htpp:// path
        yield scrapy.Request(absolute_next_page_url)