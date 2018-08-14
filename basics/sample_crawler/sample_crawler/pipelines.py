# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class SampleCrawlerPipeline(object):
    def process_item(self, item, spider):
        os.chdir('D:/Images')
        
        if item['images'][0]['path']:
                new_image_name = item['title'][0] + '.jpg'
                new_image_path = "D:/Images/full/" + new_image_name
                
                
                os.rename(item['images'][0]['path'], new_image_path)


#z = "D:/Images/full/"
#print(os.path.exists(z))