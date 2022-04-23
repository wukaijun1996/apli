#-*- codeing = utf-8 -*-
# @Time : 2022/4/23 23:02 
# @Author : wu
# @File : test_02.py 
# @Software: PyCharm

def add(a,b):
    return a+b

def div(a,b):
    return a/b

def test_add():
    assert add(3,2) == 5
    assert add(-1,2) == 1
    assert add(-2,-10) == -12

def test_div():
    assert div(3,1) == 3
    assert div(20,4) == 5






