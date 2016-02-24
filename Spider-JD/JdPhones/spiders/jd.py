# -*- coding: utf-8 -*-
import scrapy
import json

from JdPhones.items import JdphonesItem

class JDSpider(scrapy.Spider):
    name = 'jd'
    start_urls = ['http://list.jd.com/list.html?cat=9987%2C653%2C655']

    def parse(self, response):
        total = response.css(".p-wrap span.p-skip b::text").extract()[0]
        for i in range(int(total)):
            full_url = response.url+"&page="+str(i+1)
            yield scrapy.Request(full_url, callback=self.parse_phone_page)

    def parse_phone_page(self, response):
        for item in response.css("div#plist .gl-item"): 
            sku = item.css("div::attr(data-sku)").extract()[0]
            name = item.css(".p-name em::text").extract()[0]
            comments_num = int(item.css(".p-commit a::text").extract()[0])
            priceUrl = 'http://p.3.cn/prices/mgets?skuIds=J_' + sku + 'J_'

            item = JdphonesItem()
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

            # yield {
            #     "sku": sku,
            #     "name": name,
            #     "price": price["value"],
            #     "comments_num": comments_num
            # }

    def parsePrice(self, response):
        item = response.meta['item']
        try:
            item["price"] = float(json.loads(response.body)[0]['p'])
        except Exception, e:
            item["price"] = 0
        finally:
            return item
