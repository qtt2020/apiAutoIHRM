import logging
import unittest
import requests
from parameterized import parameterized

from api.emp_api import Emp
from api.login_api import Login
import app
from uitls import assert_emp, get_case_data


class TestEmployeeParams(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 实例化登录接口
        cls.login = Login()
        # 实例化员工接口
        cls.emp = Emp()

    def setUp(self) -> None:
        # 实例化session对象
        self.session = requests.session()

    def tearDown(self) -> None:
        # 关闭session
        self.session.close()

    def test01_login(self):
        # 调用登录接口
        response_login = self.login.get_login(self.session, "13800000002", "123456")
        jsonData = response_login.json()
        # 获取令牌
        token = "Bearer " + jsonData.get("data")
        logging.info("员工模块登录信息为：{}".format(jsonData))
        headers = {"Content-Type": "application/json", "Authorization": token}
        app.HEADERS = headers
        # 断言结果：响应状态码，success，code，message
        assert_emp(self, response_login, 200, True, 10000, "操作成功！")

    # 调用员工接口 添加员工
    filename = app.BASE_DIR + "/data/add_emp.json"

    @parameterized.expand(get_case_data(filename))
    def test02_add_emp(self, username, password, status_code, success, code, message):
        response_add_emp = self.emp.get_add_emp(self.session, app.HEADERS, username, password)
        # 获取登录响应数据
        jsonData = response_add_emp.json()
        # 获取响应数据的id值
        emp_id = dict(jsonData.get("data")).get("id")
        app.EMP_ID = emp_id
        logging.info("员工模块添加源信息为：{}".format(jsonData))
        # 断言结果：响应状态码，success，code，message
        assert_emp(self, response_add_emp, status_code, success, code, message)

    # 调用员工接口 查询员工
    filename = app.BASE_DIR + "/data/show_emp.json"

    @parameterized.expand(get_case_data(filename))
    def test03_show_emp(self, status_code, success, code, message):
        response_show_emp = self.emp.get_show_emp(self.session, app.HEADERS, app.EMP_ID)
        logging.info("员工模块查询员工信息为：{}".format(response_show_emp.json()))
        # 断言结果：响应状态码，success，code，message
        assert_emp(self, response_show_emp, status_code, success, code, message)

    # 调用员工接口 修改员工
    filename = app.BASE_DIR + "/data/upData_emp.json"

    @parameterized.expand(get_case_data(filename))
    def test04_upData_emp(self, username, status_code, success, code, message):
        response_upData_emp = self.emp.get_upData_emp(self.session, app.HEADERS, username, app.EMP_ID)
        logging.info("员工模块修改员工信息为：{}".format(response_upData_emp.json()))
        # 断言结果：响应状态码，success，code，message
        assert_emp(self, response_upData_emp, status_code, success, code, message)

    # 调用员工接口 删除员工
    filename = app.BASE_DIR + "/data/delete_emp.json"

    @parameterized.expand(get_case_data(filename))
    def test05_delete_emp(self, status_code, success, code, message):
        response_delete_emp = self.emp.get_delete_emp(self.session, app.HEADERS, app.EMP_ID)
        logging.info("员工模块删除员工信息为：{}".format(response_delete_emp.json()))
        # 断言结果：响应状态码，success，code，message
        assert_emp(self, response_delete_emp, status_code, success, code, message)

# # 导包
# import unittest, logging, app
# import requests
#
#
# # 创建测试类集成unittest.TestCase
# class TestEmployee(unittest.TestCase):
#
#     # 初始化unittest的函数
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass
#
#     # 创建测试函数
#
#     def test01_emp_management(self):
#         # 初始化日志
#         app.init_log()
#         # 调用登陆
#         response = requests.post("http://182.92.81.159/api/sys/login",
#                                  json={"mobile": "13800000002", "password": "123456"})
#         # 打印登陆结果
#         logging.info("员工模块的登陆结果为：{}".format(response.json()))
#         # 取出令牌，并拼接成以Bearer 开头的字符串
#         token = "Bearer " + response.json().get('data')
#         logging.info("取出的令牌为：{}".format(token))
#
#         # 设置员工模块所需要的请求头
#         headers = {"Content-Type": "application/json", "Authorization": token}
#         logging.info("员工模块请求头为：{}".format(headers))
#
#         # 调用添加员工
#         response_add_emp = requests.post("http://182.92.81.159/api/sys/user",
#                                          json={"username": "王健林supperstar33438",
#                                                "mobile": "14587532886",
#                                                "timeOfEntry": "2020-02-01",
#                                                "formOfEmployment": 1,
#                                                "departmentName": "酱油2部",
#                                                "departmentId": "1205026005332635648",
#                                                "correctionTime": "2020-02-03T16:00:00.000Z"},
#                                          headers=headers)
#         logging.info("添加员工接口的结果为：{}".format(response_add_emp.json()))
#         # 断言结果：响应状态码，success，code，message
#         self.assertEqual(200, response_add_emp.status_code)
#         self.assertEqual(True, response_add_emp.json().get("success"))
#         self.assertEqual(10000, response_add_emp.json().get("code"))
#         self.assertIn("操作成功", response_add_emp.json().get("message"))
#
#         # 由于添加员工成功后，还需要保存员工ID给后续的查询、修改、删除员工使用，所以我们需要保存员工ID
#         emp_id = response_add_emp.json().get("data").get("id")
#         logging.info("保存的员工ID为：{}".format(emp_id))
#
#         # 调用查询员工
#         query_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
#         response_query = requests.get(query_url,
#                                       headers=headers)
#         logging.info("查询员工的结果为：{}".format(response_query.json()))
#         # 断言结果：响应状态码，success，code，message
#         self.assertEqual(200, response_add_emp.status_code)
#         self.assertEqual(True, response_add_emp.json().get("success"))
#         self.assertEqual(10000, response_add_emp.json().get("code"))
#         self.assertIn("操作成功", response_add_emp.json().get("message"))
#
#         # 调用修改员工
#         modify_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
#         response_modify = requests.put(modify_url,
#                                        json={"username": "new_tom"},
#                                        headers=headers)
#         logging.info("修改员工结果为：{}".format(response_modify.json()))
#         # 断言结果：响应状态码，success，code，message
#         self.assertEqual(200, response_add_emp.status_code)
#         self.assertEqual(True, response_add_emp.json().get("success"))
#         self.assertEqual(10000, response_add_emp.json().get("code"))
#         self.assertIn("操作成功", response_add_emp.json().get("message"))
#
#         # 调用删除员工
#         delete_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
#         response_delete = requests.delete(delete_url, headers=headers)
#         logging.info("删除员工的结果为：{}".format(response_delete.json()))
#         # 断言结果：响应状态码，success，code，message
#         self.assertEqual(200, response_add_emp.status_code)
#         self.assertEqual(True, response_add_emp.json().get("success"))
#         self.assertEqual(10000, response_add_emp.json().get("code"))
#         self.assertIn("操作成功", response_add_emp.json().get("message"))
