#-*- codeing = utf-8 -*-
# @Time : 2022/4/24 22:08 
# @Author : wu
# @File : test_05_paramlize.py 
# @Software: PyCharm

import pytest

# 参数化

@pytest.mark.parametrize('test_input,result',[
    ('1+2',3),
    ('2*3', 5),
    ('pow(2,3)', 8),
])
def test_eval(test_input,result):
    assert eval(test_input) == result





