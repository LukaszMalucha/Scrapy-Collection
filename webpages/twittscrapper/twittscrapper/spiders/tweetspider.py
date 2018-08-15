# -*- coding: utf-8 -*-
import scrapy
import json


class TweetspiderSpider(scrapy.Spider):
    name = 'tweetspider'
    allowed_domains = ['trumptwitterarchive.com']
    start_urls = ['http://www.trumptwitterarchive.com/data/realdonaldtrump/2017.json']

    def parse(self, response):
        jsonresponse = json.loads(response.body)
        
        for tweet in jsonresponse:
            yield { 'created_at': tweet['created_at'],
                   'favorite_count': tweet['favorite_count']
                    }
