# -*- coding: utf-8 -*-
import  pymysql
from dytt import settings


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#格式化输出到本地
# class DyttPipeline(object):
#     def process_item(self, item, spider):
#         output = '''
#
#         ===%s===
#         %s
#         %s
#         %s
#         %s
#         简介：
#             %s
#         下载地址：
#             %s
#         ==================
#         '''%(item['filmname'],item['filmnamecn'],item['filmnameen'],item['filmyears'],item['filmtype'],item['filmintroduction'],item['filmurl'])
#         f = open("dytt.txt","a+")
#         f.write(output)
#         f.close()
#         return item

#输出到mysql
# CREATE TABLE `dyttmovie` (
#   `filmname` varchar(100) NOT NULL,
#   `filmnamecn` varchar(100) DEFAULT NULL,
#   `filmnameen` varchar(100) DEFAULT NULL,
#   `filmyears` varchar(25) DEFAULT NULL,
#   `filmtype` varchar(25) DEFAULT NULL,
#   `filmintroduction` varchar(1024) DEFAULT NULL,
#   `filmurl` varchar(256) DEFAULT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8
class DyttPipeline(object):
    def __init__(self):
        self.conncet = pymysql.connect(
            host = settings.MYSQL_HOST,
            port = 3306,
            db = settings.MYSQL_DBNAME,
            user = settings.MYSQL_USER,
            passwd = settings.MYSQL_PASSWD,
            charset = 'utf8',
            use_unicode = True
        )
        self.cursor = self.conncet.cursor()
    def process_item(self, item, spider):
        self.findtext(item)
        try:
            self.cursor.execute(
                '''select * from dyttmovie where filmurl = %s
                ''',item['filmurl'])
            repetition  =  self.cursor.fetchone()

            if repetition:
                pass
            else:
                self.cursor.execute('''insert into dyttmovie  value (%s, %s, %s, %s, %s, %s,%s)
                ''',(item['filmname'],item['filmnamecn'],item['filmnameen'],item['filmyears'],item['filmtype'],item['filmintroduction'],item['filmurl'])

                )
            self.conncet.commit()
        except Exception as error:
            pass
        return  item

    def findtext(self,item):
            self.fendict = {"filmintroduction":"◎简",'filmtype':'◎类', 'filmyears': '◎年','filmnameen':'◎片','filmnamecn':'◎译'}
            for key,fen in self.fendict.items():
                self.findtextf(key, fen, item)


    def findtextf(self ,key,fen,item):
            try:
                # filmindex = filmtext.index(fen)
                # log("*******%s******"%filmindex)
                filmtext = item['filmtext']
                for i in range(len(filmtext)):
                    if str(filmtext[i]).find(fen)>=0:
                        if key =="filmintroduction":
                            item[key] = filmtext[i+1]
                        else:
                            item[key] = filmtext[i]

                # if fen == '◎简\u3000\u3000介':
                #     item[key] = filmtext[filmindex + 1].strip()
                # else:
                #     item[key] = filmtext[filmindex].strip()
            except:
                item[key] = "暂无"

    # def findtext(self,item):
    #     item['filmnamecn'] = item['filmtext'][1]

