#-*- codeing = utf-8 -*-
# @Time : 2022/4/24 21:37 
# @Author : wu
# @File : test_04_fixture_params.py 
# @Software: PyCharm
import json,pytest

class TestParamsDemo1():
    users = [{'name': 'tony', 'password': '123456'}, {'name': 'wu', 'password': '212122'}, {'name': 'li', 'password': '2232'}]

    @pytest.fixture(params=users)    #参数化fixture允许提供参数 参数必须是可迭代对象
    def user(self,request):
        return request.param

    def test_user_pwd(self,user):
        pwd = user['password']
        assert len(pwd) >= 6

class TestParamsDemo2():
    users = json.loads(open('users_dev.json','r').read())

    @pytest.fixture(params=users)    #参数化fixture允许提供参数 参数必须是可迭代对象
    def user(self,request):
        return request.param

    def test_user_pwd(self,user):
        pwd = user['password']
        assert len(pwd) >= 6




