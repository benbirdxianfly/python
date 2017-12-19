# 写入文件

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class ZlzpPipeline(object):
#     def process_item(self, item, spider):
#         output = '''
#
#         ===%s===
#         职位名称：%s
#         工作地点：%s
#         职位月薪：%s
#         发布日期：%s
#         最低学历：%s
#         招聘人数：%s
#         职位类别：%s
#         工作经验：%s
#         连接地址：%s
#         #######################################
#         职位描述：%s
#         ######################################
#         '''%(item['gsmc'],item['zwmc'],item['gzdd'],item['zwyx'],item['fbrq'],item['zdxl'],item['zprs'],item['zwlb'],item['gzjy'],item['zwurl'],item['zwms'])
#         # print(output)
#         f = open("zlzp.txt", "a+")
#         f.write(output.replace(u'\xa0', u' '))
#         f.close()
#         return item


# 写入数据库
import pymysql
from zlzp import settings

# CREATE TABLE `zlzp` (
#   `zwmc` varchar(100) NOT NULL,
#   `gsmc` varchar(100) DEFAULT NULL,
#   `gzdd` varchar(100) DEFAULT NULL,
#   `zwyx` varchar(24) DEFAULT NULL,
#   `fbrq` varchar(32) DEFAULT NULL,
#   `zdxl` varchar(32) DEFAULT NULL,
#   `zprs` varchar(32) DEFAULT NULL,
#   `zwlb` varchar(32) DEFAULT NULL,
#   `gzjy` varchar(32) DEFAULT NULL,
#   `zwms` varchar(2048) DEFAULT NULL,
#   `zwurl` varchar(256) DEFAULT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8
class ZlzpPipeline(object):
    def __init__(self):
        self.conncet = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=3306,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.conncet.cursor()

    def process_item(self, item, spider):

        try:
            self.cursor.execute(
                '''select * from zlzp where zwurl = %s
                ''', item['zwurl'])
            repetition = self.cursor.fetchone()

            if repetition:
                pass
            else:
                self.cursor.execute('''insert into zlzp  value (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s)
                ''',(item['zwmc'],item['gsmc'],item['gzdd'],item['zwyx'],item['fbrq'],item['zdxl'],item['zprs'],item['zwlb'],item['gzjy'],item['zwms'],item['zwurl'])

                                    )
            self.conncet.commit()
        except Exception as error:
            pass
        return item
