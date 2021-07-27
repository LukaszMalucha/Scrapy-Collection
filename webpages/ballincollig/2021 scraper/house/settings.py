# -*- coding: utf-8 -*-


BOT_NAME = 'house'

SPIDER_MODULES = ['house.spiders']
NEWSPIDER_MODULE = 'house.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 24 * 60 * 60
