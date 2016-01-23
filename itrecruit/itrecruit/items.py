# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItrecruitItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TencentItem(scrapy.Item):
    name = scrapy.Field()
    catalog = scrapy.Field()
    workLocation = scrapy.Field()
    recruitNumber = scrapy.Field()
    detailLink = scrapy.Field()
    publishTime = scrapy.Field()
    pass
