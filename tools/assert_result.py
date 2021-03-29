# -*- coding:utf-8 _*-
from tools.pylog import MyLog
from tools.dict_value import res

"""期望值与实际结果做判断"""
def assert_in(assertexcepted, assertresult):
    if len(assertexcepted.split('=')) > 1:
        data = assertexcepted.split('&')
        result = dict([(item.split('=') for item in data)])
        value1 =([(str(res(assertresult, key))) for key in result.keys()])
        value2 = ([(str(value)) for value in result.values()])
        if value1 == value2:
            return {'code':0, 'result':'pass'}
        else:
            return {'code':1, 'result':'fail'}
    else:
        MyLog().info('请填写测试期望值！')
        return {'code':2, 'result':'请填写期望值'}