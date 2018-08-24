# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.loader import ItemLoader
from heroes.items import HeroesItem


class HotsSpider(scrapy.Spider):
	name = 'hots'
	allowed_domains = ['heroesofthestorm.com']
	start_urls = ['http://heroesofthestorm.com/']

	def start_requests(self):
		self.driver = webdriver.Chrome('D:/PYTHON/WebScraping/chromedriver')
		self.driver.get('https://heroesofthestorm.com/en-us/heroes/#/')

		sel = Selector(text = self.driver.page_source)
		heroes = sel.xpath('//*[@class="hero-link"]/@href').extract()
		for hero in heroes:
			url = 'https://heroesofthestorm.com/en-us/heroes/' + hero
			yield Request(url, callback=self.parse_details)


	def parse_details(self, response):
		l = ItemLoader(item=HeroesItem(), response=response)


		## GENERAL
		name 		= response.xpath('normalize-space(//h1[@class="hero-identity__name page__title"]/text())').extract_first()
		title		= response.xpath('//*[@class="hero-identity__title paragraph__heading--alternate ng-binding"]/text()').extract_first()
		description = response.xpath('//*[@class="hero-description paragraph__description ng-binding"]/text()').extract_first()
		image_urls  = response.xpath('.//meta[@property="og:image"]/@content').extract_first()

		universum	= response.xpath('//*[@class="hero-identity clearfix"]/child::div/@class').extract_first()
		universum   = universum.split('_franchise-icon ')[1]

		hero_class  = response.xpath('//*[@class="hero-role-wrapper"]/child::div/@class').extract_first()
		hero_class  = hero_class.split('icon--')[1]

		## STATS	
		damage = response.xpath('//*[contains(text(), "Damage")]/following-sibling::div/@class').extract_first()
		damage = damage.split('fill')[1]

		utility = response.xpath('//*[contains(text(), "Utility")]/following-sibling::div/@class').extract_first()
		utility = utility.split('fill')[1]

		survivability = response.xpath('//*[contains(text(), "Survivability")]/following-sibling::div/@class').extract_first()
		survivability = survivability.split('fill')[1]

		complexity = response.xpath('//*[contains(text(), "Complexity")]/following-sibling::div/@class').extract_first()
		complexity = complexity.split('fill')[1]	

		stats = {'damage': damage,
		 'utility': utility,
		 'survivability': survivability,
		 'complexity': complexity}	


		## SKILLS
		skills = response.xpath('//*[@class="ability-tooltip__title"]/text()').extract()				
		heroics = skills[0:2]
		if len(skills) == 6:	   ## Abathur, Hammer
			abilities = skills[2:5]	
		else:
			abilities = skills[2:4]	
		hero_trait = skills[-1]	

			

		skillset = {'heroics': heroics,
					'abilities': abilities,
					'hero_trait': hero_trait}	
    



		l.add_value('name', name)
		l.add_value('title', title)
		l.add_value('hero_class', hero_class)
		l.add_value('description', description)
		l.add_value('universum', universum)
		l.add_value('stats', stats)
		l.add_value('skillset', skillset)
		l.add_value('image_urls', image_urls)	
		return l.load_item()

