'''
菜鸟级别，大神略过
获取电影天堂最新电影的ftp地址
运行一次就行，，，次数多了就容易被封ip了
'''
#引入模块
from bs4 import BeautifulSoup
import requests

def Get_Data(UrlBase):
    BasePage = requests.get(UrlBase)
    # print(BasePage.encoding)#查看编码格式
    # 基础页面数据，gbk解码
    BasePageData = BasePage.content.decode('gbk')
    # soup基础页面数据
    soup = BeautifulSoup(BasePageData, "html.parser")
    # print(soup.prettify())#格式化输出
    return soup

def Get_downurl(NewFilmeList):
    for i in NewFilmeList:
        #获得电影基础网址
        Fbaseurl = UrlBase + i["href"]
        soup2=Get_Data(Fbaseurl)
        Downfurl=soup2.find('td',attrs={'style':"WORD-WRAP: break-word"})
        #输出下载地址
        if Downfurl is  not None:
            Downfurllist = Downfurl.find_next('a')
            DownUrl = Downfurllist.text
        else:
            continue
        with open("dy.txt","a+",encoding="gbk") as f:
            f.write(DownUrl+'\n')

def Get_dy(UrlBase):
    #获取基础页面信息
    soup = Get_Data(UrlBase)
    # print(soup.prettify())#格式化输出
    #找到最新电影模块
    NewFilme =soup.find('div',attrs={'class': 'co_content2'})
    #找到下属列表
    NewFilmeList = NewFilme.find_all_next('a')
    #输出下载地址
    Get_downurl(NewFilmeList)



if __name__ == '__main__':
    # 设置网址基地址
    UrlBase = "http://www.dytt8.net/"
    Get_dy(UrlBase)



