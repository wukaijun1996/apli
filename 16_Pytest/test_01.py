#-*- codeing = utf-8 -*-
# @Time : 2022/4/23 22:49 
# @Author : wu
# @File : test_01.py 
# @Software: PyCharm



def reverse(str):
    return str[::-1]

def test_reverse01(): #测试用例
    print("实时拉你")
    # assert reverse('god') == 'dog'

def test_reverse02(): #测试用例
    assert reverse('hello') == 'dog'

def test_reverse03(): #测试用例
    assert reverse('hello') == 'olleh'





