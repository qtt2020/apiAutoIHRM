import logging
import unittest
import requests
import app
from api.department_api import Department
from api.login_api import Login
from uitls import assert_emp, OperationSql


class TestDepartment(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 实例化登录接口
        cls.login = Login()
        # 实例化部门接口
        cls.department = Department()
        cls.operation_sql = OperationSql()

    def setUp(self) -> None:
        # 实例化session对象
        self.session = requests.session()

    def tearDown(self) -> None:
        # 关闭session
        self.session.close()

    # 调用登录接口
    def test01_login(self):
        response_login = self.login.get_login(self.session, "13800000002", "123456")
        jsonData = response_login.json()
        # 获取令牌
        token = "Bearer " + jsonData.get("data")
        logging.info("员工模块登录信息为：{}".format(jsonData))
        headers = {"Content-Type": "application/json", "Authorization": token}
        app.HEADERS = headers
        # 断言结果：响应状态码，success，code，message
        assert_emp(self, response_login, 200, True, 10000, "操作成功！")

    # 调用获取所有部门信息接口
    def test02_department_message(self):
        response_department = self.department.get_department(self.session, app.HEADERS)
        jsonData = response_department.json()
        # logging.info("所有部门信息为：{}".format(response_department.json()))

    # 调用添加部门接口
    def test03_add_department(self):
        response_add_department = self.department.get_add_department(self.session, app.HEADERS, "技术部1025", "1025")
        logging.info("添加部门信息为：{}".format(response_add_department.json()))
        # 数据库操作
        show_message = self.operation_sql.show_sql("select * from co_department where `name`= '技术部1025';")
        department_id = show_message[0]
        app.DEPARTMENT_ID = "/" + department_id
        # 断言结果：响应状态码，success，code，message
        assert_emp(self, response_add_department, 200, True, 10000, "操作成功！")
        self.assertEqual("技术部1025", show_message[3])

    # 调用获取指定部门信息接口
    def test04_department_message(self):
        response_department_message = self.department.get__department_message(self.session, app.HEADERS,
                                                                              app.DEPARTMENT_ID)
        logging.info("所有指定信息为：{}".format(response_department_message.json()))
        # 断言结果：响应状态码，success，code，message
        assert_emp(self, response_department_message, 200, True, 10000, "操作成功！")

    # 调用修改部门信息接口
    def test05_upData_department(self):
        response_upData_department = self.department.get_upData_department(self.session, app.HEADERS, "技术部1998",
                                                                           app.DEPARTMENT_ID)
        logging.info("修改部门信息为：{}".format(response_upData_department.json()))
        # 数据库操作
        show_message = self.operation_sql.show_sql("select * from co_department where `name`= '技术部1998';")
        # 断言结果：响应状态码，success，code，message
        assert_emp(self, response_upData_department, 200, True, 10000, "操作成功！")
        self.assertEqual("技术部1998", show_message[3])

    # 调用获取指定部门信息接口
    def test06_delete_department(self):
        response_delete_department = self.department.get__delete_department(self.session, app.HEADERS,
                                                                            app.DEPARTMENT_ID)
        logging.info("所有指定信息为：{}".format(response_delete_department.json()))
        # 数据库操作
        show_message = self.operation_sql.show_sql("select * from co_department where `name`= '技术部1998';")
        # 断言结果：响应状态码，success，code，message
        assert_emp(self, response_delete_department, 200, True, 10000, "操作成功！")
        self.assertEqual(None, show_message)
