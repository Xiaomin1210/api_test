import jsonpath
from tools.pylog import MyLog

class AssertResult():

    def __init__(self, excepted, actual):
        self.excepted = excepted
        self.actual = actual

    def assert_true(self):
        for info in eval(self.excepted):
            print(info)
            actual_str = jsonpath.jsonpath(self.actual, info['jsonPath'])[0]
            excepted_str = info['excepted']
            MyLog().info('预期结果：{} 实际结果：{}'.format(excepted_str,actual_str))
            if actual_str == excepted_str:
                return True
            else:
                return False

if __name__ == '__main__':
    excepted = "[{'jsonPath':'$.status','excepted':1}]"
    actual = {'status': 1, 'msg': '', 'data': {'token': '5344-KT3A9F3B4CB48651F5B7ECAD3947758D8F', 'uid': 5344, 'nickname': '我要喝可乐', 'gender': 0, 'avatar': 'https://images.e-gets.io/upload/default/member_face.png', 'language': 1, 'bind_id': 0, 'mobile': '85516273817', 'uuid': 8616626858229760, 'u_token': 'QJqqROU5GV0DXyUvxwDp3c74n17U14PB', 'u_token_expired_at': 0, 'today_login_out_times': 0, 'country_code': '855', 'sns_bind': '', 'created_new_password': ''}}

    print(AssertResult(excepted, actual).assert_true())