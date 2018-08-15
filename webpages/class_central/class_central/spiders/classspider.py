# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class ClassSpiderSpider(scrapy.Spider):
    name = 'classspider'
    allowed_domains = ['class-central.com']
    start_urls = ['http://class-central.com/subjects']
    
    
    
    def __init__(self, subject=None):
        self.subject = subject
                         
    def parse(self, response):
        if self.subject:
            subject_url = response.xpath('//*[contains(@title, "' + self.subject + '")]/@href').extract_first()
            yield Request(response.urljoin(subject_url), callback=self.parse_subject)
        else:
            self.logger.info('Scraping all subjects.')
            subjects = response.xpath('//*[@class="show-all-subjects view-all-courses"]/@href').extract() 
            for subject in subjects:
                yield Request(response.urljoin(subject), callback=self.parse_subject)
        
    def parse_subject(self, response):
        subject_name = response.xpath('//title/text()').extract_first()
        subject_name = subject_name.split(' | ')
        subject_name = subject_name[0]
        
        courses = response.xpath('//*[@itemtype="http://schema.org/Event"]')
        for course in courses:
            course_name = course.xpath('.//*[@itemprop="name"]/text()').extract_first()
            course_url = course.xpath('.//*[@itemprop="url"]/@href').extract_first()
            absolute_course_url = response.urljoin(course_url)
            
            yield {'subject_name': subject_name,
                   'course_name': course_name, 
                   'absolute_course_url': absolute_course_url
                    }
            
        next_page = response.xpath('//*[@rel="next"]/@href').extract_first()
        absolute_next_page = response.urljoin(next_page)
        yield Request(absolute_next_page, callback=self.parse_subject)