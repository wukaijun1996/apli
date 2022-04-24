#-*- codeing = utf-8 -*-
# @Time : 2022/4/23 23:17 
# @Author : wu
# @File : test_03.py 
# @Software: PyCharm

import json
import pytest

# [
#   {"name":"tony","password":"123456"},
#   {"name":"wu","password":"212122"},
#   {"name":"li","password":"342232"}
# ]
# s = '[{"name":"tony","password":"123456"}]'
# # print(type(s))
# s1 = json.loads(s)
# print(type(s1))

# with open("./users_dev.json","r") as f:
#     print(f.read())
#     print(type(f.read()))
#     a = json.loads(f.read())
#     # print(a)

a = open('./users_dev.json','r').read()
print(a)
print(type(a))
content = json.loads(a)
print(content)
print(type(content))
for i in content:
    print(i.get('password'))


class TestUserPwd():
    @pytest.fixture()
    def users(self):
        return json.loads(open("users_dev.json","r").read())

    def test_user_pwd(self,users):
        for user in users:
            pwd = user['password']
            assert len(pwd) >= 6







