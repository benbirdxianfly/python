# -*- coding: utf-8 -*-
import scrapy
from zlzp.items import ZlzpItem

class ZpSpider(scrapy.Spider):
    name = 'zp'
    allowed_domains = ['zhaopin.com']
    address = ['天津','北京']
    work = ['运维工程师','测试工程师','开发工程师']
    start_urls = []
    for i in  address:
        for j in work:
            print(i,j)
            start_urls.append('''https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%s&kw=%s&sm=0&p=1'''%(i,j))
            print(start_urls)

    # print(start_urls)
    # start_urls = ['https://sou.zhaopin.com/jobs/searchresult.ashx?jl=天津&kw=测试工程师&sm=0&p=1']


    def parse(self, response):
        for zw in response.xpath('//table[@class="newlist"]'):
            zwurl = zw.xpath('./tr[1]/td[1]/div/a[1]/@href').extract_first()
            if  zwurl:
                yield scrapy.Request(zwurl, callback=self.parse_next)
        page_down_url  = response.xpath('//a[@class="next-page"]/@href').extract_first()
        # print(page_down_url)
        yield scrapy.Request(page_down_url, callback=self.parse)



    def parse_next(self,response):
        zwxq =  ZlzpItem()
        zwxq['zwurl'] = response.url
        zwxq['zwmc'] = response.xpath('/html/body/div[5]/div[1]/div[1]/h1/text()').extract_first()
        zwxq['gsmc'] = response.xpath('/html/body/div[5]/div[1]/div[1]/h2/a/text()').extract_first()
        zwxq['zwyx'] = response.xpath('//ul[@class="terminal-ul clearfix"]/li[1]/strong/text()').extract_first()
        zwxq['gzdd'] = response.xpath('//ul[@class="terminal-ul clearfix"]/li[2]/strong/a/text()').extract_first()
        zwxq['fbrq'] = response.xpath('//ul[@class="terminal-ul clearfix"]/li[3]/strong/span/text()').extract_first()
        zwxq['gzjy'] = response.xpath('//ul[@class="terminal-ul clearfix"]/li[5]/strong/text()').extract_first()
        zwxq['zdxl'] = response.xpath('//ul[@class="terminal-ul clearfix"]/li[6]/strong/text()').extract_first()
        zwxq['zprs'] = response.xpath('//ul[@class="terminal-ul clearfix"]/li[7]/strong/text()').extract_first()
        zwxq['zwlb'] = response.xpath('//ul[@class="terminal-ul clearfix"]/li[8]/strong/a/text()').extract_first()
        ms = []
        for p in response.xpath('//div[@class="tab-inner-cont"]/p'):
            a = str(p.xpath('text()').extract_first()).strip()
            if a:
                if a != 'None':
                    ms.append(a)
        zwxq['zwms'] = ''.join(ms)

        # print(zwxq['zwmc'])
        # print(zwxq['gsmc'])
        # print(zwxq['zwyx'])
        # print(zwxq['gzdd'])
        # print(zwxq['fbrq'])
        # print(zwxq['zdxl'])
        # print(zwxq['zprs'])
        # print(zwxq['zwlb'])
        # print(zwxq['zwms'])
        yield zwxq


