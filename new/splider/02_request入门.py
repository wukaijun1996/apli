#-*- codeing = utf-8 -*-
# @Time : 2022/1/8 17:30 
# @Author : wu
# @File : 02_request入门.py 
# @Software: PyCharm

import requests

url = "https://fanyi.baidu.com/sug"

s = input("请输入你要翻译的英文单词")

data = {
     "kw": s
 }

resp = requests.post(url,data=data,)

print(resp.json())
print(resp.text)





