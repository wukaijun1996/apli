#-*- codeing = utf-8 -*-
# @Time : 2022/4/23 23:02 
# @Author : wu
# @File : test_02.py 
# @Software: PyCharm
import pytest


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


#断言异常抛出
def test_zero_div1():
    with pytest.raises(ZeroDivisionError):
        div(5,0)
#允许访问异常的具体信息，并且对他断言
def test_zero_div2():
    with pytest.raises(ZeroDivisionError) as zero:
        div(5,0)
    assert 'division by zero' in str(zero.value)


