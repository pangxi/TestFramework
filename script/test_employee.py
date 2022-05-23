import json
import unittest

import requests

import app

from api.employee import EmployeeAPI



from utils import common_assert


# 创建测试类
class TestEmployee(unittest.TestCase):
    # 保存员工id
    employee_id = None

    # 前置处理器
    def setUp(self):
        # 实例化接口类
        self.employee_api = EmployeeAPI()


    # 添加员工
    def test_add_employee(self):
        add_employee_data = {
            "username" : "tom6454",      # 用户名唯一
            "mobile" : "13800008181",    # 手机号唯一
            "workNumber" : "16880524",   # 员工号唯一
            "timeOfEntry" : "2022-05-23",
            "formOfEmployment" : 1,
            "departmentId" : "1111",
            "departmentName" : "技术部",
            "correctionTime" : "2022-05-24"
        }
        response  = self.employee_api.add_employee(add_employee_data=add_employee_data)
        print(response.json())

        # 断言
        common_assert(self,response)

        # 保存员工id
        TestEmployee.employee_id = response.json().get("data").get("id")
        print(TestEmployee.employee_id)

    # 查询员工
    def test_get_employee(self):
        response = self.employee_api.get_employee(TestEmployee.employee_id)
        print(response.json())
        # 断言
        common_assert(self,response)

    # 修改员工
    def test_updata_employee(self):
        updata = {"username" : "tom0"}
        response = self.employee_api.update_employee(TestEmployee.employee_id,updata=updata)
        print(response.json())
        # 断言
        common_assert(self,response)

    # 删除员工
    def test_del_employee(self):
        response = self.employee_api.del_employee(TestEmployee.employee_id)
        print(response.json())
        # 断言
        common_assert(self,response)







if __name__ == "__main__":
	# 运行所有的用例
    unittest.main()