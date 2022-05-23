import json
import unittest

import requests

import app

from api.login import LoginAPI
from parameterized import parameterized
from utils import common_assert





# 构造数据
def build_data():
    file = app.BASE_DIR + "/data/login.json"
    test_data = []
    with open(file,encoding="utf-8") as f:
        # 加载json文件数据
        json_data = json.load(f)
        for case_data in json_data:
            login_data = case_data.get("login_data")
            status_code = case_data.get("status_code")
            success = case_data.get("success")
            code = case_data.get("code")
            message = case_data.get("message")
            test_data.append((login_data,status_code,success,code,message))
    return test_data

# 创建测试类
class TestLogin(unittest.TestCase):

    # 前置处理器
    def setUp(self):
        # 实例化接口类
        self.login = LoginAPI()
        # 创建session对象
        self.session = requests.Session()

    # 后置处理器
    def tearDown(self):
        if self.session:
            self.session.close()

    # 正常登录用例
    def test_login(self):
        login_data = {
            "mobile": "13800000002",
            "password": "123456"
        }
        response  = self.login.login(login_data)
        print(response.json())

        # 断言
        common_assert(self, response)

        # 保存token信息
        app.TOKEN = "Bearer " + response.json().get("data")
        print(app.TOKEN)
        app.headers_data["Authorization"] = app.TOKEN
        print(app.headers_data["Authorization"])

    # 登录异常用例
    @parameterized.expand(build_data)
    def test_login_abnormal(self, login_data, status_code, success, code, message):
        response = self.login.login(login_data)
        print(response.json())

        # 断言
        common_assert(self, response, status_code, success, code, message)



if __name__ == "__main__":
	# 运行所有的用例
    unittest.main()
