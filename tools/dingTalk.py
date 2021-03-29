# -*- coding:utf-8 _*-

from tools.http_requests import Http_requests
from test_data.helper import dingtalk_url
import json
"""封装一个钉钉机器人"""

def dingTalkRobot(content):
    dingdingtalk_url = dingtalk_url

    pagrem = {
              "msgtype": "text",
              "text": {
                "content": content,
                "mentioned_list": ["laiyunmin",],
              }
             }
    res = Http_requests().http_requests(url=dingdingtalk_url, data=json.dumps(pagrem), http_method='post')
    if res.status_code == 200:
        return True
    else:
        return False


if __name__ == '__main__':
    dingTalkRobot()