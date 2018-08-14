# -*- coding: utf-8 -*-
import os
import glob
from scrapy import Spider                                        ## gathering urls 
from scrapy.http import Request


def product_info(response, value):
        return response.xpath('//th[text()="' + value + '"]/following-sibling::td/text()' ).extract_first()



class Crawler2Spider(Spider):                                              
    name = 'crawler2'
    allowed_domains = ['books.toscrape.com']
#    start_urls = ['http://books.toscrape.com']

    ## CATEGORY SELECTOR
#    def __init__(self, category):
#            self.start_urls = [category]
    ## scrapy crawl books -a category="http://books.toscrape.com/catalogue/category/books/classics_6/index.html"
    
                    
    def parse(self, response):
            books = response.xpath('//h3/a/@href').extract()             
            for book in books:
                    absolute_url = response.urljoin(book)                      ## get full url path 
                    yield Request(absolute_url, callback=self.parse_book)  
                    
            ## next page
            next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
            absolute_next_page_url = response.urljoin(next_page_url)
            yield Request(absolute_next_page_url)
                 
    def parse_book(self, response):
             title = response.xpath('//h1/text()').extract_first()
             price = response.xpath('//*[@class="price_color"]/text()').extract_first()
             img_url = response.xpath('//img/@src').extract_first()                 
             img_url = img_url.replace('../..', 'http://books.toscrape.com/')  ## fixing url
             rating = response.xpath('//*[contains(@class, "star-rating")]/@class').extract_first()
             rating = rating.replace('star-rating ', '')
             description = response.xpath('//*[@id="product_description"]/following-sibling::p/text()').extract_first()
             
             # data-points
             upc = product_info(response, 'UPC' )
             product_type = product_info(response, 'Product Type')
             
             
             yield {'title': title,
                    'price': price,
                    'img_url': img_url,
                    'rating': rating,
                    'description': description,  
                    'upc' : upc,
                    'product_type' : product_type
                   }
      
    def closed(self, reason):
             csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)
             os.rename(csv_file, 'asdasd.csv')
             
             
             