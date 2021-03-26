# -*- coding:utf-8 _*-
# -*- coding:utf-8 _*-
import unittest
from ddt import ddt,data
from tools.do_excel import Do_excel
from tools.project_path import ProjectPath
from tools.pylog import MyLog
from tools.http_requests import Http_requests
from test_data.helper import globals_data



my_logger = MyLog()
test_data = Do_excel().get_data(ProjectPath.test_data_path, 'Sheet1')

@ddt
class TestAddAddrs(unittest.TestCase):

    def setUp(self):
        my_logger.info('测试用例开始执行！')
        print('开始执行测试用例！！！')


    @data(*test_data)
    def test_api(self, items):
        my_logger.info(items)
        my_logger.info(globals_data)
        replace_data = ['NONE','TOKEN','addr_id']
        for j in replace_data:
            if items['data'].find('$'+j) != -1:
                items['data'] = items['data'].replace('$'+j, globals_data[j])
            # if items['result'].find('$'+j) != -1:
            #     items['data'] = items['data'].replace('$'+j,globals_data[j])
            # elif items['result'].find('$'+j) != -1:
            #     items['data']
        my_logger.info(items)
        res = Http_requests().http_requests(items['url'], eval(items['data']), items['http_method'], cookie=None, headers=eval(items['headers']))


        my_logger.info('正在执行测试用例！!!')
        my_logger.info('正在执行{0}测试用例'.format(items['title']))
        my_logger.info('============================测试结果============================')
        my_logger.info('这是测试返回的结果{0}'.format(res.json()))
        # my_logger.info('这是添加的收货地址id：{0}'.format(res.json()['data']['addr_id']))
        excepted_data = res.json()
        for key in excepted_data.keys():
            # if excepted_data[excepted_key_data]:
            # my_logger.info(type(excepted_data[key]['addr_id']))
            # my_logger.info(type(excepted_data[key]['addr_id']))
            try:
                if key == 'data':
                    globals_data['addr_id'] = str(eval(excepted_data['data']['addr_id']))
            except Exception as e:
                raise e


        # if res.json()['error']:
        #     globals_data['addr_id'] = res.json()['error']
        # # elif res.json()['error']:
        # #     pass

        try:
            self.assertEqual(str(items['excepted']), str(res.json()['error']))
            TestResult = 'Pass'

        except AssertionError as e:
            my_logger.error('测试用例报错啦！{0}'.format(e))
            TestResult = 'Faile'

        finally:
            Do_excel().write_back(ProjectPath.test_data_path, 'Sheet1', int(items['case_id'] + 1), str(res.json()),
                                  TestResult)
            return res

    def tearDown(self):
        my_logger.info('============================测试用例执行完毕！============================')
        print('测试用例执行完毕！！！')

if __name__ == '__main__':
    unittest.main()