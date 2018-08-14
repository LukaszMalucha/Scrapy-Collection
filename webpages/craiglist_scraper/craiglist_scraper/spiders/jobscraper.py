# -*- coding: utf-8 -*-
import scrapy


class JobscraperSpider(scrapy.Spider):
    name = 'jobscraper'
    allowed_domains = ['newyork.craigslist.org']
    start_urls = ['https://newyork.craigslist.org/d/software-qa-dba-etc/search/sof']

    def parse(self, response):
        
            
        ## listings basics    
        listings = response.xpath('//li[@class="result-row"]')
        for listing in listings:
            date = listing.xpath('.//*[@class="result-date"]/@datetime').extract_first()
            link = listing.xpath('.//a[@class="result-title hdrlnk"]/@href').extract_first()
            text = listing.xpath('.//a[@class="result-title hdrlnk"]/text()').extract_first()


            yield scrapy.Request(link,
                                 callback=self.parse_listing,
                                 meta={'date': date,                            ## meta dictionary
                                       'link': link,
                                       'text': text})    

            
        ## move to next page    
        next_page_url = listing.xpath('//*[@title="next page"]/@href').extract_first()    
        next_page_url = response.urljoin(next_page_url)
        if next_page_url:
                yield scrapy.Request(next_page_url, callback=self.parse)
            
    def parse_listing(self, response):
        date = response.meta['date']
        link = response.meta['link']
        text = response.meta['text']
        
        compensation = response.xpath('//*[@class="attrgroup"]/span[1]/b/text()').extract_first()
        employment_type = response.xpath('//*[@class="attrgroup"]/span[2]/b/text()').extract_first()
        images = response.xpath('//*[@id="thumbs"]//@src').extract()
        images = [image.replace('50x50c', '600x450') for image in images]               ## change resolution 
        description = response.xpath('//*[@id="postingbody"]/text()') .extract()        ## double slash not needed
        
        
        yield {'date': date,
               'link': link,
               'text': text,
               'compensation': compensation,
               'employment_type': employment_type,
               'images': images,
               'description': description}
   