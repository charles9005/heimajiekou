import unittest
from requests import Session
from api.login import LoginApi
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()
    def setUp(self):
        self.session = Session()
    def tearDown(self):
        self.session.close()
    def test_login_success(self):
        #正确的用户名和密码
        response = self.login_api.login(self.session, "13800000002", "123456")
        result =response.json()
        self.assertEqual(True,result.get("success"))
    def test_login_no_mobile(self):
        # 空的用户名和密码
        response = self.login_api.login(self.session, "", "123456")
        result = response.json()
        self.assertEqual(False, result.get("success"))
        self.assertEqual(20001,result.get("code"))
    def test_login_no_passwd(self):
        # 空的密码
        response = self.login_api.login(self.session, "13800000002", "")
        result = response.json()
        self.assertEqual(False, result.get("success"))
        self.assertEqual(20001, result.get("code"))
    def test_login_wrong_passwd(self):
        #错误的密码
        response = self.login_api.login(self.session, "13800000002", "111111")
        result = response.json()
        self.assertEqual(False, result.get("success"))
        self.assertEqual(20001, result.get("code"))
    def test_login_wrong_username(self):
        #错误的用户名
        response = self.login_api.login(self.session, "13812344322", "123456")
        result = response.json()
        self.assertEqual(False, result.get("success"))
        self.assertEqual(20001, result.get("code"))


