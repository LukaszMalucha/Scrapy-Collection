# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class TablescraperSpider(scrapy.Spider):
    name = 'tablescraper'
    allowed_domains = ['basketball-reference.com']
    start_urls = ['https://basketball-reference.com/players/']

    def parse(self, response):
        players_urls = response.xpath('//li/a[contains(@href,"players/")]/@href').extract()[1:-1]
        for url in players_urls:
            url = 'https://basketball-reference.com' + url
            yield Request(url, callback=self.parse_table)
    
    def parse_table(self, response):
        player_rows = response.xpath('//tr')[1:]
        for row in player_rows:
            name = row.xpath('.//th/a/text()').extract_first()
            birth = row.xpath('.//td[6]/a/text()').extract_first()
            colleges = row.xpath('.//td[7]/a/text()').extract_first()            
            yield {'name': name, 'birth': birth, 'colleges': colleges}

            
            