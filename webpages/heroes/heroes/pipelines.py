# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import re

class HeroesPipeline(object):
	def process_item(self, item, spider):
		os.chdir('D:/heroes/Images')

		if item['images'][0]['path']:
			new_image_name = item['name'][0]
			new_image_name = re.sub('[\/:<>*?"|]', '', new_image_name)
			new_image_name = new_image_name + '.jpg'
			new_image_path = "full/" + new_image_name
			os.rename(item['images'][0]['path'], new_image_path)	

