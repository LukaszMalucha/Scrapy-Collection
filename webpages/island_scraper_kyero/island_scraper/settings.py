# -*- coding: utf-8 -*-
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

software_names = [SoftwareName.FIREFOX.value]
operating_systems = [OperatingSystem.WINDOWS.value] 

user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

BOT_NAME = 'island_scraper'

SPIDER_MODULES = ['island_scraper.spiders']
NEWSPIDER_MODULE = 'island_scraper.spiders'


# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'
USER_AGENT = user_agent_rotator.get_random_user_agent()


ROBOTSTXT_OBEY = False

FEED_EXPORT_FIELDS = ['title','island','locality','price','beds','size', 'link', 'date', 'ad_type']