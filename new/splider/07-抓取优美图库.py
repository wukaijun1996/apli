#-*- codeing = utf-8 -*-
# @Time : 2022/1/10 21:06 
# @Author : wu
# @File : 07-抓取优美图库.py 
# @Software: PyCharm

import requests,time
from bs4 import BeautifulSoup

url = "https://www.umei.cc/tags/dxmv.htm"

resp = requests.get(url)
# with open("优美图片网页源码.html","w",encoding="utf-8") as fp:
#     fp.write(resp.text)
# print(resp.text)
soup = BeautifulSoup(resp.text,"lxml")

TypeList = soup.find("div",attrs={'class':'TypeList'})
# print(TypeList)
TypeBigPics = TypeList.find_all(attrs={"class":"TypeBigPics"})
# print(TypeBigPics)
head_url = "https://www.umei.cc"
for one_picture in TypeBigPics:
    one_picture_url = head_url + one_picture.get("href")
    # print(one_picture_url)
    resp_one = requests.get(one_picture_url)
    soup_one = BeautifulSoup(resp_one.text,"lxml")
    ret = soup_one.find("div",attrs={'class':'ImageBody'})
    # print(ret)
    ret = ret.find("img").get("src")
    print(ret)

    pict_name = ret.split(r"/")[-1]
    pict = requests.get(ret)

    with open("image/" + pict_name, "wb") as fp:
        fp.write(pict.content)
    time.sleep(1)

print("抓取完毕")


















