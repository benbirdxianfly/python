# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#定义需要获取内容
class DyttItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    filmtext = scrapy.Field()
    filmname = scrapy.Field()
    filmnamecn = scrapy.Field()
    filmnameen = scrapy.Field()
    filmyears = scrapy.Field()
    filmtype = scrapy.Field()
    filmintroduction = scrapy.Field()
    filmurl = scrapy.Field()
