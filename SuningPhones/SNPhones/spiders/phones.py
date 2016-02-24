# -*- coding: utf-8 -*-
import scrapy
import json
import re

from SNPhones.items import SnphonesItem

class PhoneSpider(scrapy.Spider):
    name = 'phones'
    start_urls = ['http://list.suning.com/0-20006-0-0-0-9017.html']

    def parse(self, response):
        total = response.css(".snPages #pageLast::text").extract()[0]

        for i in range(int(total)):
            full_url = 'http://list.suning.com/0-20006-' + str(i) + '-0-0-9017.html'
            yield scrapy.Request(full_url, callback=self.parse_phone_page)

    def parse_phone_page(self, response):
        for item in response.css("div#proShow .items .item"): 
            sku = item.css(".i-price p.price::attr(datasku)").extract()[0]
            sku = sku[:len(sku)-3]
            # price = item.css(".i-price strong::text").extract()[0]
            name = item.css(".i-name .sellPoint::text").extract()[0]
            comments_num_str = item.css(".i-stock span.com-cnt::text").extract()[0]
            
            comments_num = int(comments_num_str[:len(comments_num_str)-3])
            priceUrl = 'http://ds.suning.cn/ds/prices/000000000' + sku + '-9017--1-SES.product.priceCenterCallBack.jsonp'


            item = SnphonesItem()
            item["sku"] = sku
            item["name"] = name
            item["comments_num"] = comments_num

            # item = {
            #     "sku": sku,
            #     "name": name,
            #     "comments_num": comments_num
            # }

            request = scrapy.Request(priceUrl,callback=self.parsePrice)
            request.meta['item'] = item
            yield request

    def parsePrice(self, response):
        item = response.meta['item']
        try:
            responseJson  = re.sub(r'([a-zA-Z_0-9\.]*\()|(\);?$)','',response.body)
            item["price"] = float(json.loads(responseJson)['rs'][0]['price'])
        except Exception, e:
            item["price"] = 0
        finally:
            return item
