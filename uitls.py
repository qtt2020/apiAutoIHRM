import json

import pymysql

import app
from app import BASE_DIR


def assert_emp(self, response, status_code, success, code, message):
    # 断言结果：响应状态码，success，code，message
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))


class OperationSql:
    _conn = None
    _cursor = None

    # 获取连接数据库
    @classmethod
    def get_connect_sql(cls):
        if cls._conn is None:
            cls._conn = pymysql.connect("182.92.81.159", "readuser", "iHRM_user_2019", "ihrm")
        return cls._conn

    # 获取创建游标
    @classmethod
    def get_newCursor(cls):
        if cls._cursor is None:
            cls._cursor = cls.get_connect_sql().cursor()
        return cls._cursor

    # 关闭数据库连接
    @classmethod
    def close_sql_connect(cls):
        if cls._conn is not None:
            cls.get_connect_sql().close()
            cls._conn = None

    # 关闭游标
    @classmethod
    def close_cursor(cls):
        if cls._cursor is not None:
            cls.get_newCursor().close()
            cls._cursor = None

    # 操作数据库
    @classmethod
    def show_sql(cls, sql):
        try:
            # 创建游标
            cursor = cls.get_newCursor()
            cursor.execute(sql)
            data = cursor.fetchone()
        except Exception as e:
            raise e
        finally:
            cls.close_cursor()
            cls.close_sql_connect()
        return data


# q = OperationSql()
# print(q.show_sql("select * from co_department where `name`= '技术部';"))

def get_case_data(filename):
    with open(filename, encoding="utf_8") as f:
        jsonData = json.load(f)
    case_list = list()
    for case in jsonData.values():
        case_list.append(tuple(case.values()))
    return case_list






