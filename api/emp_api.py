class Emp:
    def __init__(self):
        self.emp_url = "http://182.92.81.159/api/sys/user/"
        self.login_url = "http://182.92.81.159/api/sys/login"

    # 登录
    def get_login(self, session, mobile, password):
        data = {"mobile": mobile, "password": password}
        headers = {"Content-Type": "application/json"}
        return session.post(self.login_url, headers=headers, json=data)

    # 添加员工
    def get_add_emp(self, session, headers, username, mobile):
        data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2019-07-01",
            "formOfEmployment": 1,
            "workNumber": "1322131",
            "departmentName": "开发部",
            "departmentId": "1066240656856453120",
            "correctionTime": "2019-11-30"
        }
        return session.post(self.emp_url, json=data, headers=headers)

    # 查询员工
    def get_show_emp(self, session, headers, emp_id):
        return session.get(self.emp_url + emp_id, headers=headers)

    # 修改员工
    def get_upData_emp(self, session, headers, username, emp_id):
        data = {"username": username}
        return session.put(self.emp_url + emp_id, headers=headers, json=data)

    # 删除员工
    def get_delete_emp(self, session, headers, emp_id):
        return session.delete(self.emp_url + emp_id, headers=headers)
