# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QuotesSpiderPipeline(object):
	def process_item(self, item, spider):
		if item['author']:
			item['author'] = item['author'][0].lower()
		return item
