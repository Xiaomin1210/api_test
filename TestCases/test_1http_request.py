# -*- coding:utf-8 _*-
import unittest,logger
from ddt import ddt,data
from tools.do_excel import Do_excel
from tools.project_path import ProjectPath
from tools.pylog import MyLog
from tools.http_requests import Http_requests
from tools.get_cookie import GetCookie
from test_data import helper
from tools.assert_result import AssertResult


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

        my_logger.info(items['excepted'])
        my_logger.info(res.json())

        helper.globals_data['TOKEN'] = res.json()['data']['token']
        print(helper.globals_data)

        try:
            test_rusult = (AssertResult(excepted=items['excepted'], actual=res.json()).assert_true())
            if test_rusult == True:
                write_result = 'pass'
            elif test_rusult == False:
                write_result = 'fail'
        except Exception as e:
            my_logger.info('断言出错啦！，错误如下: %s' % e)
        finally:
            Do_excel().write_back(ProjectPath.test_data_path, 'login', int(items['case_id'] + 1), str(res.json()),
                                  write_result)
            return res
        my_logger.info('正在执行测试用例！!!')
        my_logger.info('正在执行{0}测试用例'.format(items['title']))
        my_logger.info('============================测试结果============================')
        my_logger.info('这是测试返回的结果{0}'.format(res.json()))

    def tearDown(self):
        my_logger.info('============================测试用例执行完毕！============================')
        print('测试用例执行完毕！！！')

if __name__ == '__main__':
    unittest.main()