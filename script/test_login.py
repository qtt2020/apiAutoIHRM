import logging
import unittest
import requests
from parameterized import parameterized

from api.login_api import Login
from app import BASE_DIR
from uitls import assert_emp, get_case_data


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 实例化登录接口
        cls.login = Login()

    def setUp(self) -> None:
        # 实例化session对象
        self.session = requests.session()

    def tearDown(self) -> None:
        # 关闭session
        self.session.close()

    filename = BASE_DIR + "/data/login.json"

    @parameterized.expand(get_case_data(filename))
    # 登录成功
    def test01_login_success(self, mobile, password, status_code, success, code, message):
        # 调用登录接口
        response = self.login.get_login(self.session, mobile, password)
        logging.info("员工模块登录信息为：{}".format(response.json()))
        # 断言结果：响应状态码，success，code，message
        assert_emp(self, response, status_code, success, code, message)

    # # 用户名不存在
    # def test02_mobile_error(self):
    #     # 调用登录接口
    #     response = self.login.get_login(self.session, "18379204795", "123456")
    #     logging.info("员工模块登录用户名不存在信息为：{}".format(response.json()))
    #     # 断言结果：响应状态码，success，code，message
    #     assert_emp(self, response, 200, False, 20001, "用户名或密码错误")
    #
    # # 密码错误
    # def test03_password_error(self):
    #     # 调用登录接口
    #     response = self.login.get_login(self.session, "18379204795", "123456")
    #     logging.info("员工模块登录密码错误信息为：{}".format(response.json()))
    #     # 断言结果：响应状态码，success，code，message
    #     assert_emp(self, response, 200, False, 20001, "用户名或密码错误")
    #
    # # 用户名为空
    # def test04_mobile_is_none(self):
    #     # 调用登录接口
    #     response = self.login.get_login(self.session, "", "123456")
    #     logging.info("员工模块登录用户名为空信息为：{}".format(response.json()))
    #     # 断言结果：响应状态码，success，code，message
    #     assert_emp(self, response, 200, False, 20001, "用户名或密码错误")
    #
    # # 密码为空
    # def test05_password_is_none(self):
    #     # 调用登录接口
    #     response = self.login.get_login(self.session, "13800000002", "")
    #     logging.info("员工模块登录密码为空信息为：{}".format(response.json()))
    #     # 断言结果：响应状态码，success，code，message
    #     assert_emp(self, response, 200, False, 20001, "用户名或密码错误")
    #
    # # 少mobile参数
    # def test06_less_mobile_params(self):
    #     # 调用登录接口
    #     response = self.login.get_params_login(self.session, {"password": "123456"})
    #     logging.info("员工模块登录少mobile参数信息为：{}".format(response.json()))
    #     # 断言结果：响应状态码，success，code，message
    #     assert_emp(self, response, 200, False, 20001, "用户名或密码错误")
    #
    # # 少password参数
    # def test06_less_password_params(self):
    #     # 调用登录接口
    #     response = self.login.get_params_login(self.session, {"mobile": "13800000002"})
    #     logging.info("员工模块登录少password参数信息为：{}".format(response.json()))
    #     # 断言结果：响应状态码，success，code，message
    #     assert_emp(self, response, 200, False, 20001, "用户名或密码错误")
    #
    # # 多参
    # def test07_many_params(self):
    #     # 调用登录接口
    #     response = self.login.get_params_login(self.session, {"mobile": "13800000002", "password": "123456", "a": "1"})
    #     logging.info("员工模块登录多参信息为：{}".format(response.json()))
    #     # 断言结果：响应状态码，success，code，message
    #     assert_emp(self, response, 200, True, 10000, "操作成功！")
    #
    # # 错参
    # def test08_error_params(self):
    #     # 调用登录接口
    #     response = self.login.get_params_login(self.session, {"mboile": "13800000002", "password": "123456"})
    #     logging.info("员工模块登录错参信息为：{}".format(response.json()))
    #     # 断言结果：响应状态码，success，code，message
    #     assert_emp(self, response, 200, False, 20001, "用户名或密码错误")
    #
    # # 无参
    # def test09_not_params(self):
    #     # 调用登录接口
    #     response = self.session.post("http://182.92.81.159/api/sys/login")
    #     logging.info("员工模块登录无参信息为：{}".format(response.json()))
    #     # 断言结果：响应状态码，success，code，message
    #     assert_emp(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！")
