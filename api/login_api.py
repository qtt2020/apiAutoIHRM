class Login:
    def __init__(self):
        self.login_url = "http://182.92.81.159/api/sys/login"

    # 登录
    def get_login(self, session, mobile, password):
        data = {"mobile": mobile, "password": password}
        headers = {"Content-Type": "application/json"}
        return session.post(self.login_url, headers=headers, json=data)

    # 针对参数的登录测试
    def get_params_login(self, session, json):
        headers = {"Content-Type": "application/json"}
        return session.post(self.login_url, headers=headers, json=json)


