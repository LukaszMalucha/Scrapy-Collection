# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.loader import ItemLoader
from hots_scraper.items import HotsScraperItem



    


class HeroesSpider(scrapy.Spider):
    name = 'heroes'
    allowed_domains = ['heroesofthestorm.gamepedia.com']
    start_urls = ['https://heroesofthestorm.gamepedia.com/Heroes_of_the_Storm_Wiki']

    def parse(self, response):
        heroes_urls = response.xpath('//*[@class="link"]/a/@href').extract() 
        for url in heroes_urls:
            url = 'https://heroesofthestorm.gamepedia.com' + url
            yield Request(url, callback=self.parse_hero)

     
    def parse_hero(self, response):
        l = ItemLoader(item=HotsScraperItem(), response=response)
        
        name = response.xpath('//*[@id="firstHeading"]/text()').extract_first()
        role = response.xpath('//tr/th[contains(text(),"Role")]/following-sibling::td/a/text()').extract_first()
        universum = response.xpath('//tr/th[contains(text(),"Franchise")]/following-sibling::td/a/@title').extract_first()
        abilities = response.xpath('//*[@class="skill-name"]/text()').extract()        
        image_urls = response.xpath('//a[@class="image"]/img/@src').extract_first()

        l.add_value('name', name)
        l.add_value('role', role)
        l.add_value('universum', universum)
        l.add_value('abilities', abilities)
        l.add_value('image_urls', image_urls)        
        return l.load_item()
