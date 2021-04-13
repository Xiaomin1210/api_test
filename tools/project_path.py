# -*- coding:utf-8 _*-
import os
import time

# 获取项目的绝对路径
class ProjectPath:

    project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

    # 测试文件的路径
    test_data_path = os.path.join(project_path, 'test_data', 'test_data.xlsx')
    nowtime = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    # 测试报告的路径
    # test_result_path = os.path.join(project_path, 'testResult', '{0}_test_html.html'.format(nowtime))
    test_result_path = os.path.join(project_path, 'testResult', 'test_result.html')

    # 配置文件的路径
    test_conf_path = os.path.join(project_path, 'conf', 'conf.config')

if __name__ == '__main__':
    path = ProjectPath.test_result_path
    print(path)
