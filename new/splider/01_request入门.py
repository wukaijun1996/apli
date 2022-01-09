#-*- codeing = utf-8 -*-
# @Time : 2022/1/8 16:31 
# @Author : wu
# @File : request入门.py 
# @Software: PyCharm

import requests

url = "https://movie.douban.com/top250"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

resp = requests.get(url,headers=headers)

# print(resp.text)
html = resp.text
with open("bilibili.html","w",encoding="utf-8") as fp :
    fp.write(html)

print(resp.url)
print("爬取完毕")