#-*- codeing = utf-8 -*-
# @Time : 2022/1/9 19:03 
# @Author : wu
# @File : 04_re模块.py 
# @Software: PyCharm

import re

lst = re.findall(r"\d+","我的电话号是：10010,我问等级考试寄快递：10086")
print(lst)


#返回迭代器
it = re.finditer(r"\d+","我的电话号是：10010,我问等级考试寄快递：10086")
print(it)
for i in it:
    print(i.group())

#找到一个结果就返回
s = re.search(r"\d+","我的电话号是：10010,我问等级考试寄快递：10086")
print(s.group())

#从头开始匹配
s = re.match(r"\d+","我的电话号是：10010,我问等级考试寄快递：10086")
print(s)

obj = re.compile(r"\d+")
ret = obj.finditer("我的电话号是：10010,我问等级考试寄快递：10086")
print(ret)















