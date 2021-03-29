# -*- coding:utf-8 _*-
import unittest,logger
from ddt import ddt,data
from tools.do_excel import Do_excel
from tools.project_path import ProjectPath
from tools.pylog import MyLog
from tools.http_requests import Http_requests
from tools.get_cookie import GetCookie
from test_data import helper
from tools.assert_result import assert_in

my_logger = MyLog()
test_data = Do_excel().get_data(ProjectPath.test_data_path, 'login')


@ddt
class Test_1_HttpRequest(unittest.TestCase):
    def setUp(self):
        my_logger.info('测试用例开始执行！')
        print('开始执行测试用例！！！')


    @data(*test_data)
    def test_1_api(self, items):
        res = Http_requests().http_requests(items['url'], eval(items['data']), items['http_method'], getattr(GetCookie,
                                                                                                       'cookie'), eval(items['headers']))
        # if res.json()['data']['token']:
            # my_logger.info('获取的token为{0}'.format(res.json()['data']['token']))
            # Context.globals_data['TOKEN'] = res.json()['data']['token']
        # if res.cookies:
        #     setattr(GetCookie, 'cookie', res.cookies)
        # elif res.json()['data']['token']:
        #     my_logger.info('获取的token为{0}'.format(res.json()['data']['token']))
        #     Context.globals_data['TOKEN'] = res.json()['data']['token']
        # elif res.json()['msg']:
        #     my_logger.info('登录失败')
        # res.status_code == 200:
            # my_logger.info('获取的token为{0}'.format(res.json()['data']['token']))
        assert_res = assert_in(assertexcepted=items['excepted'], assertresult=res.json())
        if assert_res['code'] == 0:
            my_logger.info('pass')
        elif assert_res['code'] == 1:
            my_logger.info('fail')
        my_logger.info(assert_res)
        helper.globals_data['TOKEN'] = res.json()['data']['token']
        print(helper.globals_data)
        # setattr(GetCookie, 'TOKEN', res.json()['data']['token'])


        my_logger.info('正在执行测试用例！!!')
        my_logger.info('正在执行{0}测试用例'.format(items['title']))
        my_logger.info('============================测试结果============================')
        my_logger.info('这是测试返回的结果{0}'.format(res.json()))




        # excepted_data = eval(items['excepted'])  #期望值
        # for key in excepted_data.keys():
        #     excepted_data_key = key
        #
        # try:
        #     self.assertEqual(excepted_data[excepted_data_key], res.json()[excepted_data_key])
        #     my_logger.info('这个是从excel中获取的断言数据：'+ str(excepted_data[excepted_data_key]))
        #     my_logger.info('这个是从响应中获取的实际数据：' + str(res.json()[excepted_data_key]))
        #     TestResult = 'Pass'
        #
        #
        # except AssertionError as e:
        #     my_logger.error('测试用例报错啦！{0}'.format(e))
        #     TestResult = 'Fail'
        #
        # finally:
        #     Do_excel().write_back(ProjectPath.test_data_path, 'login', int(items['case_id'] + 1), str(res.json()),
        #                           TestResult)
        #     return res
        #



    def tearDown(self):
        my_logger.info('============================测试用例执行完毕！============================')
        print('测试用例执行完毕！！！')

if __name__ == '__main__':
    unittest.main()