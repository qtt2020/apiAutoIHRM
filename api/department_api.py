class Department:
    def __init__(self):
        self.department_url = "http://182.92.81.159/api/company/department"

    # 获取所有部门信息
    def get_department(self, session, headers):
        return session.get(self.department_url, headers=headers)

    # 获取指定部门信息
    def get__department_message(self, session, headers, department_id):
        return session.get(self.department_url+department_id, headers=headers)

    # 添加部门
    def get_add_department(self, session, headers, name, code):
        data = {"name": name, "code": code}
        return session.post(self.department_url, headers=headers, json=data)

    # 修改部门
    def get_upData_department(self, session, headers, name, department_id):
        data = {"name": name}
        return session.put(self.department_url + department_id, json=data, headers=headers)

    # 获取指定部门信息
    def get__delete_department(self, session, headers, department_id):
        return session.delete(self.department_url + department_id, headers=headers)





