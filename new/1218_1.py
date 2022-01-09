#-*- codeing = utf-8 -*-
# @Time : 2021/12/18 18:05 
# @Author : wu
# @File : 1218_1.py 
# @Software: PyCharm
import re

# re.match('^p.*','python is language')
# if re.match('^p.*','python is language'):
#     print(re.match('^p.*','python is language').group())
# res = re.match('([0-9]*)-(\d*)','0123-456789')
# print(res.group(2))
data = "华为人是华人的骄傲"

# rs = re.compile('华.')
# rs_1 = rs.match(data)
# print(rs_1.group())

# rs = re.search('华.*人',data)
# print(rs.group())


# rs = re.findall('华.',data)
# print(rs)

data = '百度 ，腾讯 ，阿里 ，华为 ，360'
print(re.split('阿',data))


















