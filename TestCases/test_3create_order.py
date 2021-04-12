# -*- coding:utf-8 _*-
import unittest
from ddt import ddt,data
from tools.do_excel import Do_excel
from tools.project_path import ProjectPath
from tools.pylog import MyLog
from tools.http_requests import Http_requests
from test_data.helper import globals_data
from tools.assert_result import AssertResult



my_logger = MyLog()
test_data = Do_excel().get_data(ProjectPath.test_data_path, 'createorder')

@ddt
class TestCreateOrder(unittest.TestCase):

    def setUp(self):
        my_logger.info('测试创建订单用例开始执行！')
        print('开始执行测试用例！！！')


    @data(*test_data)
    def test_api(self, items):
        my_logger.info(items)
        my_logger.info(globals_data)
        replace_data = ['NONE','TOKEN','addr_id','order_id']
        for j in replace_data:
            if items['headers'].find('$'+j) != -1:
                items['headers'] = items['headers'].replace('$'+j, globals_data[j])

            if items['data'].find('$'+j) != -1:
                items['data'] = items['data'].replace('$'+j, globals_data[j])

        my_logger.info(items)
        res = Http_requests().http_requests(items['url'], eval(items['data']), items['http_method'], headers=eval(items['headers']))
        try:
            res.json()['data']['order_id']
            globals_data['order_id'] = str(res.json()['data']['order_id'])
        except:
            pass
        #
        my_logger.info('正在执行{0}测试用例'.format(items['title']))
        my_logger.info('============================测试结果============================')
        my_logger.info('这是测试返回的结果{0}'.format(res.json()))

        # my_logger.info('这是添加的收货地址id：{0}'.format(res.json()['data']['addr_id']))

        try:
            test_rusult = (AssertResult(excepted=items['excepted'], actual=res.json()).assert_true())
            if test_rusult == True:
                write_result = 'pass'
            elif test_rusult == False:
                write_result = 'fail'
        except Exception as e:
            my_logger.info('断言出错啦！，错误如下: %s' % e)
        finally:
            Do_excel().write_back(ProjectPath.test_data_path, 'createorder', int(items['case_id'] + 1), str(res.json()),
                                  write_result)
            return res

    def tearDown(self):
        my_logger.info('============================测试用例执行完毕！============================')
        print('测试用例执行完毕！！！')

if __name__ == '__main__':
    unittest.main()