#api/login.py
import requests
class LoginApi:
    def __init__(self):
        self.url = "http://ihrm-test.itheima.net/api/sys/login"
    def login(self,session,mobile,password):
        data ={
            "mobile":mobile,
            "password":password
        }
        return session.post(self.url,json=data)
#调试用
# session =requests.session()
# print(LoginApi().login(session, "13800000002", "123456").json())