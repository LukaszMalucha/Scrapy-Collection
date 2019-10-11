# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.loader import ItemLoader
from kilkenny.items import KilkennyItem



class JewelsSpider(Spider):
	name = 'jewels'
	allowed_domains = ['www.kilkennyshop.com']
	start_urls = ['https://www.kilkennyshop.com/default/brand/?p=1']


	def parse(self, response):
		urls = ('https://www.kilkennyshop.com/default/brand/?p={}'.format(i) for i in range(1,30)) #29
		for url in urls:
			yield Request(url, callback=self.parse_products)


	def parse_products(self, response):
		products = response.xpath('//*[@class="zoo-inner-product-item-info"]')
		for product in products:
			l = ItemLoader(item=KilkennyItem(), selector=product)
			product_id = str(product.xpath('.//*[@class="price-box price-final_price"]/@data-product-id').extract_first())
			name = product.xpath('.//*[@class="product-item-link"]/text()').extract_first()[1:]  ## avoid \n
			price_euro = product.xpath('.//*[@class="price"]/text()').extract_first()[1:]
			descr_1 = product.xpath('.//*[@class="product description product-item-description product_list_style"]/text()').extract_first()
			descr_2 = product.xpath('.//*[@class="product description product-item-description product_list_style"]/p/text()').extract_first()
			descr_3 = product.xpath('.//*[@class="product description product-item-description product_list_style"]/p/text()').extract()[1:]
			image_urls = product.xpath('.//img/@src').extract()


			l.add_value('product_id', product_id)	
			l.add_value('name', name)
			l.add_value('price_euro', price_euro)
			l.add_value('descr_1', descr_1)
			l.add_value('descr_2', descr_2)
			l.add_value('descr_3', descr_3)
			l.add_value('image_urls', image_urls)
			
			yield l.load_item()

			