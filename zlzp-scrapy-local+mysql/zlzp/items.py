# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZlzpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #职位名称
    zwmc = scrapy.Field()
    #公司名称
    gsmc = scrapy.Field()
    #工作地点
    gzdd = scrapy.Field()
    #职位月薪
    zwyx = scrapy.Field()
    #发布日期
    fbrq = scrapy.Field()
    #最低学历
    zdxl = scrapy.Field()
    #招聘人数
    zprs = scrapy.Field()
    #职位类别
    zwlb = scrapy.Field()
    #工作经验
    gzjy = scrapy.Field()
    # 职位描述
    zwms = scrapy.Field()
    #连接地址
    zwurl = scrapy.Field()
