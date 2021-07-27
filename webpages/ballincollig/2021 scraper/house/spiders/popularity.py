# -*- coding: utf-8 -*-
import scrapy
from pathlib import Path
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import csv
from random import randrange
from datetime import datetime
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from datetime import date

from house.items import BallincolligItem

## AVOID HANDSHAKE ERRORS
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--incognito")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

software_names = [SoftwareName.FIREFOX.value]
operating_systems = [OperatingSystem.WINDOWS.value,] 
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

today = date.today()
todays_date = today.strftime("%Y-%m-%d")

urls = [
"https://www.daft.ie/property-for-sale/ballincollig-cork?numBeds_from=3&numBeds_to=4&salePrice_to=400000&sort=publishDateDesc&salePrice_from=200000&pageSize=20&from=0",
"https://www.daft.ie/property-for-sale/ballincollig-cork?numBeds_from=3&numBeds_to=4&salePrice_to=400000&sort=publishDateDesc&salePrice_from=200000&from=20&pageSize=20"
]



class PopularitySpider(scrapy.Spider):
    name = 'popularity'
    allowed_domains = ['www.daft.ie']
    start_urls = ['https://www.daft.ie/']

    def parse(self, response):
        agent = user_agent_rotator.get_random_user_agent()
        options.add_argument(f"user-agent={agent}")
        self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
        self.driver.set_window_size(randrange(1100, 1200), randrange(800, 900))


        links = []
        for page in urls:
            agent = user_agent_rotator.get_random_user_agent()
            options.add_argument(f"user-agent={agent}")
            self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
            self.driver.set_window_size(randrange(1100, 1200), randrange(800, 900))
            self.driver.get(page)
            sleep(2)
            self.driver.get(page)
            body = self.driver.find_element_by_css_selector('body')
            sleep(1)
            body.send_keys(Keys.END)
            sleep(1)
            body.send_keys(Keys.HOME)
            sel = Selector(text=self.driver.page_source)
            adverts = sel.xpath('//li[contains(@class, "SearchPage__Result")]')
            
            for ad in adverts:
                link = ad.xpath('.//a/@href').extract_first()
                full_link = "https://www.daft.ie" + link
                links.append(full_link)


        for link in links:
            self.driver.get(link)   
            sleep(1)
            sel = Selector(text=self.driver.page_source)
            price =  sel.xpath('//span[contains(@class, "TitleBlock__StyledSpan")]/text()').extract_first()
            address = sel.xpath('//h1[contains(@class, "TitleBlock__Address")]/text()').extract_first()
            count = len(sel.xpath('//p[contains(@class, "TitleBlock__CardInfoItem")]/text()'))
            if count == 4:
                beds = sel.xpath('//p[contains(@class, "TitleBlock__CardInfoItem")]/text()')[-4].extract()
                baths = sel.xpath('//p[contains(@class, "TitleBlock__CardInfoItem")]/text()')[-3].extract() 
                size = sel.xpath('//p[contains(@class, "TitleBlock__CardInfoItem")]/text()')[-2].extract()  # MOZE NIE BYC
                property_type = sel.xpath('//p[contains(@class, "TitleBlock__CardInfoItem")]/text()')[-1].extract()
            else:
                beds = sel.xpath('//p[contains(@class, "TitleBlock__CardInfoItem")]/text()')[0].extract()
                baths = sel.xpath('//p[contains(@class, "TitleBlock__CardInfoItem")]/text()')[1].extract() 
                property_type = sel.xpath('//p[contains(@class, "TitleBlock__CardInfoItem")]/text()')[-1].extract()

            popularity = sel.xpath('//div[contains(@class, "Statistics__StyledStat")]/p/text()')[-2].extract()

            l = ItemLoader(item=BallincolligItem(), selector=sel)
            l.add_value('price', price)                     
            l.add_value('address', address)       
            l.add_value('beds', beds)
            l.add_value('baths', baths)
            l.add_value('size', size)
            l.add_value('link', link)   
            l.add_value('property_type', property_type)
            l.add_value('popularity', popularity)
            l.add_value('date', todays_date)
            yield l.load_item()   

            sleep(1)  
            
        self.driver.quit()    











                



           