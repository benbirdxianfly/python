# -*- coding: utf-8 -*-
import scrapy
from meizitu.items import MeizituItem


class MztSpider(scrapy.Spider):
    name = 'mzt'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://www.mzitu.com/all/']

    def parse(self, response):
        for urls in response.xpath('//ul[@class="archives"]/li/p[2]/a'):
            url = urls.xpath('@href').extract_first()
            yield scrapy.Request(url, callback=self.next_parse)

    def next_parse(self,response):

        # response.xpath('//div[@class="pagenavi"]/a[last()-1]/span/text()')
        # img['title'] = response.xpath('//h2[@class="main-title"]/text()').extract_first()
        max = response.xpath('//div[@class="pagenavi"]/a[last()-1]/span/text()').extract_first()
        for i in range((int(max)+1)):
            # print(i)
            imgurl = response.url + '/'+ str(i)
            yield scrapy.Request(imgurl, callback=self.img_parse)

    def img_parse(self,response):
        img = MeizituItem()
        img['title'] = response.xpath('//div[@class="main-image"]/p/a/img/@alt').extract_first()
        img['imgurl']= response.xpath('//div[@class="main-image"]/p/a/img/@src').extract_first()
        yield  img




