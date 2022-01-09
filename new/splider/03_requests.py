#-*- codeing = utf-8 -*-
# @Time : 2022/1/8 17:54 
# @Author : wu
# @File : 03_requests.py 
# @Software: PyCharm
import requests

url = "https://movie.douban.com/j/chart/top_list"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}


parm = {
    "type": 11,
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20,
}

resp = requests.get(url=url,params=parm,headers=headers)
 
print(resp.url)
print(resp.request.url)
print(resp.request.headers)
print(resp.json())
print(resp.text)