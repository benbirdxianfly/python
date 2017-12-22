# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import urllib.request
from urllib import parse
import requests

class MeizituPipeline(object):
    def process_item(self, item, spider):
        # print(item['title'],item['imgurl'])
        #判断文件夹是否存在
        mlpath = os.path.join("F:\\tu\\",item['title'])
        print(mlpath)
        if os.path.exists(mlpath):
            # 存在直接存图片
            self.saveimg(item['imgurl'],mlpath)
        else:
            #不存在，创建目录
            os.makedirs(mlpath)
            #存图片
            self.saveimg(item['imgurl'], mlpath)
        return item
    #保存图片
    def saveimg(self,url,mlpath):
        #要写上refere
        HEADERS = {
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Referer': 'http://www.mzitu.com'
        }
        urp = parse.urlparse(url)
        filename = str(urp.path).split('/')[3]
        filepath = mlpath +'\\'+ filename
        # urllib.request.urlretrieve(url, filepath)
        #加headers信息，否则看不到图片
        img = requests.get(url,headers=HEADERS, timeout=10)

        with open(filepath, 'ab') as f:
            f.write(img.content)

        f.close()