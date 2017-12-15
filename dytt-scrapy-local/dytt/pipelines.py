# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#格式化输出到本地
class DyttPipeline(object):
    def process_item(self, item, spider):
        output = '''

        ===%s===
        %s
        %s
        %s
        %s
        简介：
            %s
        下载地址：
            %s
        ==================
        '''%(item['filmname'],item['filmnamecn'],item['filmnameen'],item['filmyears'],item['filmtype'],item['filmintroduction'],item['filmurl'])
        f = open("dytt.txt","a+")
        f.write(output)
        f.close()
        return item

