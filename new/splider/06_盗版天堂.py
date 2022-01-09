#-*- codeing = utf-8 -*-
# @Time : 2022/1/9 22:55 
# @Author : wu
# @File : 06_盗版天堂.py 
# @Software: PyCharm

import requests

domain = "https://www.dytt89.com/"

resp = requests.get(domain)
resp.encoding = "gb2312"

# print(resp.text)









