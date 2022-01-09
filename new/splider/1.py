#-*- codeing = utf-8 -*-
# @Time : 2022/1/8 15:05 
# @Author : wu
# @File : 1.py 
# @Software: PyCharm

from urllib.request import urlopen

url = "http://www.douban.com/"
resp = urlopen(url)

# print(resp.read().decode("utf-8"))

html = resp.read().decode("utf-8")
with open("shouye.html", 'w',encoding="utf-8") as fp:

        fp.write(html,)
print("爬取完毕")






