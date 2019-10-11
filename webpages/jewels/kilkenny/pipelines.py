# -*- coding: utf-8 -*-
import os
import time

class KilkennyPipeline(object):
	def process_item(self, item, spider):
		os.chdir("F:/Scrapers/kilkenny/img")
		try:
			new_image_name = item['product_id'][0] + '.jpg'
			new_image_path = 'full/' + new_image_name
			os.rename(item['images'][0]['path'], new_image_path)
		except:
			pass	
