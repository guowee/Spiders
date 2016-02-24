# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutocodeItem(scrapy.Item):
    province = scrapy.Field()
    city = scrapy.Field()
    code = scrapy.Field()
    isp=scrapy.Field()
    pass




