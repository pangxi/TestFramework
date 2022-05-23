# 导包
import time
import unittest

import app
from lib.HTMLTestRunner import HTMLTestRunner
from script.test_employee import TestEmployee
from script.test_login import TestLogin


# 封装测试套件
suite = unittest.TestSuite()
# 登录接口测试用例
suite.addTest(unittest.makeSuite(TestLogin))
# 员工管理场景测试用例
suite.addTest(TestLogin("test_login"))   # 解决员工管理接口依赖登录接口问题
suite.addTest(unittest.makeSuite(TestEmployee))


# 指定测试报告路径
# report = "./report/report.html"
report = app.BASE_DIR + "/report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))


# 文件流形式打开文件
with open(report,'wb') as f:
    # 创建HTMLTestRunner的运行器
    runner = HTMLTestRunner(f,title='API Report')
    # 执行测试套件
    runner.run(suite)