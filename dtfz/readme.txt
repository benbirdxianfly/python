使用步骤 (百度 ORC)


1. 安装 ADB

2. 安装 python 3
3. 安装所需 python 包

    
urllib
    
requests
    
base64


selenium

1.在百度平台上创建应用申请 API Key 和 Secret Key

2. 在 GetTitleBaiduAndroid.py 中加入相应 key

    
# 百度OCR API
    
api_key = ''
    
api_secret = ''




运行脚本 python GetTitleBaiduAndroid.py


原地址https://github.com/Skyexu/TopSup
单独更改了安卓代码，更换为chrom浏览器，变为浏览器复用减少搜索时间