# 导包
import logging
import time
import unittest

# 实例化测试套件
from HTMLTestRunner_PY3 import HTMLTestRunner

from app import BASE_DIR
from script.test_emp_params import TestEmployeeParams
from script.test_login import TestLogin

suite = unittest.TestSuite()
# 添加测试用例到测试套件
suite.addTest(unittest.makeSuite(TestEmployeeParams))
suite.addTest(unittest.makeSuite(TestLogin))
# 设置路径
filename = BASE_DIR+"/report/ihem.html"
# 打开测试报告文件
with open(filename, "wb") as f:
    # 实例化HTMLTestRunner对象
    runner = HTMLTestRunner(stream=f, verbosity=2, title="iHRM_员工模块", description="win10")
    # 执行测试用例
    runner.run(suite)






