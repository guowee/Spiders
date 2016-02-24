# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from scrapy import Selector
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import Rule, Spider, CrawlSpider

from autocode.items import AutocodeItem


class PhoneSpider(Spider):
    name = 'phone'
    domain = "11684.net"
    start_urls = ["http://www.11684.net"]
    base_url = 'http://www.11684.net'
    start_url_list = [('浙江', '杭州', 'http://www.11684.net/city/hangzhou.php'),
                      ('浙江', '湖州', 'http://www.11684.net/city/huzhou.php'),
                      ('浙江', '宁波', 'http://www.11684.net/city/ningbo.php'),
                      ('浙江', '温州', 'http://www.11684.net/city/wenzhou.php'),
                      ('浙江', '舟山', 'http://www.11684.net/city/zhoushan.php'),
                      ('浙江', '嘉兴', 'http://www.11684.net/city/jiaxing.php'),
                      ('浙江', '金华', 'http://www.11684.net/city/jinhua.php'),
                      ('浙江', '丽水', 'http://www.11684.net/city/lishui.php'),
                      ('浙江', '衢州', 'http://www.11684.net/city/quzhou.php'),
                      ('浙江', '绍兴', 'http://www.11684.net/city/shaoxing.php'),
                      ('浙江', '台州', 'http://www.11684.net/city/taizhou305.php')]

    def parse(self, response):

        for item in self.start_url_list:
            province = item[0]
            city = item[1]
            start_url = item[2]
            yield scrapy.Request(start_url, callback=self.parse_item,
                                 meta={'province': province, 'city': city})

    def parse_item(self, response):
        sel = Selector(response)

        province = response.meta['province']
        city = response.meta['city']
        sub_url = sel.xpath('//div[@class="all"]/ul/li/a/@href').extract()
        for url in sub_url:
            start_url = self.base_url + str(url)[2:]
            yield scrapy.Request(start_url, callback=self.parse_detail,
                                 meta={'province': province, 'city': city})

    def parse_detail(self, response):

        item = AutocodeItem()
        temp = response.url.split('_')[1]
        code = filter(str.isdigit, str(temp))

        print '-----'+code[:3]
        if code[:3] in ['130', '131', '132', '155', '156', '186']:
            item['isp'] = '联通'
        elif code[:3] in ['133', '153', '189']:
            item['isp'] = '电信'
        else:
            item['isp'] = '移动'

        item['province'] = response.meta['province']
        item['city'] = response.meta['city']
        item['code'] = code

        return item
