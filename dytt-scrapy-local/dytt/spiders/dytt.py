import scrapy
from dytt.items import DyttItem


class dytt(scrapy.Spider):
    name = "dytt"
    allowed_domains = ["dytt8.net"]
    start_urls = ["http://www.dytt8.net/html/gndy/dyzz/index.html"]

#爬去新电影首页，获取详情页url
    def parse(self, response):
        for sel in response.xpath('//table[@class="tbspan"]'):
            title = sel.xpath('tr[2]/td[2]/b/a/text()').extract()
            url = sel.xpath('tr[2]/td[2]/b/a/@href').extract()
            full_url = response.urljoin(url[0])
            yield scrapy.Request(full_url, callback=self.parse_next)
            # print(title)
            # print(full_url)
        next_page_list = response.xpath('//div[@class="co_content8"]/div[@class="x"]/td/a[last()-1]/@href').extract()
        next_page = response.urljoin(next_page_list[0])
        yield scrapy.Request(next_page, callback=self.parse)



#爬取详情页信息
    def parse_next(self,response):
        item = DyttItem()
        film = response.xpath('//div[@id="Zoom"]/td/text()').extract()
        item['filmname'] = response.xpath('//title/text()').extract_first()
        item['filmnamecn'] = film[1].strip()
        item['filmnameen']= film[2].strip()
        item['filmyears'] = film[3].strip()
        item['filmtype'] = film[4].strip()
        try:
            filmindex = film.index("◎简　　介 ")
            item['filmintroduction'] = film[filmindex + 1].strip()
        except:
            item['filmintroduction'] = "暂无"
        item['filmurl'] =  response.xpath('//td[@style="WORD-WRAP: break-word"]/a/@href').extract_first()

        #测试输出
        #  print(filmname)
        # print(filmnamecn)
        # print(filmnameen)
        # print(filmyears)
        # print(filmtype)
        # print(filmurl)
        # print(filmintroduction)
        # output = '''
        #
        # ===%s===
        # %s
        # %s
        # %s
        # %s
        # 简介：
        #     %s
        # 下载地址：
        #     %s
        # ==================
        # '''%(filmname,filmnamecn,filmnameen,filmyears,filmtype,filmintroduction,filmurl)
        # print(output)
        yield item








