import requests
from tools.pylog import MyLog
import time


class Http_requests():
    def http_requests(self, url, data, http_method, cookie=None, headers=None):
        try:
            if http_method.upper() == 'GET':
                res = requests.get(url, data, cookies=cookie, headers=headers)
            elif http_method.upper() == 'POST':
                res = requests.post(url, data, cookies=cookie, headers=headers)
            else:
                print('这个请求方式暂时不支持噢~+错误原因{0}')
        except Exception as e:
            MyLog().error('这是一个暂未添加的请求方式{0}'.format(e))
            raise e
        finally:
            return res

if __name__ == '__main__':
    test_url = 'https://takeaway.e-gets.io/v1/session/login'
    test_data = {'account':'16273817','account_type':'local','country_code':'855','is_app':'1','lat':'24.6099','lng':'118.047','password':'111111','timestamp':int(time.time()),'ver':'3.1.3'}
    headers = {'content-type':'application/x-www-form-urlencoded','did':'5560985317801985'}

    robot_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c24aa118-b597-47e3-b1fc-696d91199527'
    text = {
        "msgtype": "text",
        "text": {
            "content": "广州今日天气：29度，大部分多云，降雨概率：60% + 登录提示{0}",
            "mentioned_list": ["laiyunmin", "@all"],
            "mentioned_mobile_list": ["13800001111", "@all"]
        }
    }
    text1 = {
                "msgtype": "news",
                "news": {
                   "articles" : [
                       {
                           "title" : "中秋节礼品领取",
                           "description" : "今年中秋节公司有豪礼相送",
                           "url" : "https://takeaway.e-gets.io/waimai/index.html",
                           "picurl" : "https://images.e-gets.io/upload/photo/202007/20200730_BAC2884F396B6E251B53AC4E545EB0DA.png"
                       }
                    ]
                }
            }
    text2 = {
        "msgtype": "news",
        "news": {
            "articles": [
                {
                    "title": "中秋节礼品领取",
                    "description": "今年中秋节公司有豪礼相送",
                    "url": "https://takeaway.e-gets.io/waimai/index.html",
                    "picurl": "https://images.e-gets.io/upload/photo/202007/20200730_BAC2884F396B6E251B53AC4E545EB0DA.png"
                }
            ]
        }
    }

    add_data = {'API':'client/member/addr/create','CITY_ID':'48','CLIENT_API':'CUSTOM','CLIENT_OS':'IOS','CLIENT_VER':'3.1.3.20210309.2','LANG':'cn','LAT':'11.563746','LNG':'104.911688','REGISTER_ID':'13165ffa4ebec63f212','TOKEN':'5344-KTB29D0F300920685717AE3DA795DD86B9','city_code':'','data':'{"mobile" : "0085516273817","house" : "Hhhh","contact" : "Yyy","wx_account" : "Ghhjjj","addr" : "中国福建省厦门市集美区凤岐路","lat" : "24.61277919557508","lng" : "118.0419159957075","type" : 2}','test':'1',}
    add_url = 'https://takeaway.e-gets.io/api.php'
    delete_data = {'API':'client/member/addr/delete','CITY_ID':'53','CLIENT_API':'CUSTOM','CLIENT_OS':'IOS','CLIENT_VER':'3.1.3.20210309.2','LANG':'cn','LAT':'24.610204','LNG':'118.046698','REGISTER_ID':'171976fa8a37664809a','TOKEN':'$TOKEN','city_code':'','data':'{"addr_id" : "3011","lat" : 24.610204,"lng" : 118.04669800000001}',}
    #
    # res = Http_requests().http_requests(url=add_url, data=add_data, http_method='post', headers=headers)
    # print(res.text)
    # res1 = requests.post(url=robot_url, json=text1,)
    # print(res1.text)
    # url2 = 'https://takeaway.e-gets.io/v2/order/order'
    # data2 = {'is_ziti':'0','lat':'24.61013293104972','lng':'118.0467790667441','products':' [{"product_id" : "363863","spec_id" : "","num" : 2,"ingredient" : [],"specification" : [],"package_id" : "0"}]','shop_id':'1294','ver':'3.1.4',}
    # headers2 = {'content-type':'application/x-www-form-urlencoded','did':'5560985317801985','tk':'5344-KTD5F2D1D1206C4046D47C9F8EE510FFD3',}
    #
    # res2 = Http_requests().http_requests(url=url2, data=data2, http_method='post', headers=headers2)
    # print(res2.cookies)
    # print(res2.headers)
    # print(res2.json())

    a = {'addr_id':'3112','coupon_id':'0','hongbao_id':'0','is_ziti':'0','lat':'24.61013694533942','lng':'118.0467804367667','online_pay':'1','pei_time':'尽快送达','products':'[{"product_id" : "363863","spec_id" : "","num" : 2,"ingredient" : [],"specification" : [],"package_id" : "0"}]','shop_id':'1294','ver':'3.1.4',}

    b = {'addr_id':'3112','confirmed_code':'','coupon_id':'0','hongbao_id':'0','intro':'','lat':'24.61007303923654','lng':'118.0468483144771','online_pay':'1','pei_time':'0','pei_type':'1','products':'[{"product_id" : "363863","spec_id" : "","num" : 2,"ingredient" : [],"specification" : [],"package_id" : "0"}]','remark_tag_id':'','shop_id':'1294','ver':'3.1.4',}

    c = {'API':'client/payment/order','CITY_ID':'53','CLIENT_API':'CUSTOM','CLIENT_OS':'IOS','CLIENT_VER':'3.1.4.20210323.1','LANG':'cn','LAT':'24.610129','LNG':'118.046797','REGISTER_ID':'171976fa8a37664809a','TOKEN':'$TOKEN','city_code':'','data':'{"use_money" : "0","code" : "money","order_id" : 34003,"lat" : 24.610129000000001,"lng" : 118.046797}',}