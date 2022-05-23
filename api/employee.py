# 导包
import requests

# 创建接口类
import app


class EmployeeAPI:

    # 初始化
    def __init__(self):
        self.url_add_employee = app.BASE_URL + "/api/sys/user"
        self.url_employee = app.BASE_URL + "/api/sys/user/{}"


    # 添加员工
    def add_employee(self,add_employee_data):
        return requests.post(url = self.url_add_employee,json=add_employee_data,headers=app.headers_data)

    # 修改员工
    def update_employee(self,employee_id,updata):
        url = self.url_employee.format(employee_id)
        return requests.put(url=url, json=updata, headers=app.headers_data)

    # 查询员工
    def get_employee(self,employee_id):
        url = self.url_employee.format(employee_id)
        return requests.get(url=url, headers=app.headers_data)

    # 删除员工
    def del_employee(self,employee_id):
        url = self.url_employee.format(employee_id)
        return requests.delete(url=url, headers=app.headers_data)