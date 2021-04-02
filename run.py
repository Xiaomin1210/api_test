# -*- coding:utf-8 _*-
from TestCases.test_1http_request import *
from HTMLTestRunner import HTMLTestRunner
from tools import project_path
from TestCases import test_1http_request,test_2add_addrs,test_3create_order

suite = unittest.TestSuite()

# suite.addTest(test_http_request.TestHttpRequest('test_api'))
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_1http_request))
suite.addTest(loader.loadTestsFromModule(test_2add_addrs))
suite.addTest(loader.loadTestsFromModule(test_3create_order))
with open(project_path.ProjectPath.test_result_path,'wb') as file:

    runner = HTMLTestRunner(stream=file,verbosity=2,title='xiaomei')
    runner.run(suite)