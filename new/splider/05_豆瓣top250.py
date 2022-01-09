#-*- codeing = utf-8 -*-
# @Time : 2022/1/9 21:16 
# @Author : wu
# @File : 05_豆瓣top250.py 
# @Software: PyCharm
import re
import requests
import csv
# url = "https://movie.douban.com/top250?start=0&filter="

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}


for n in range(1,2):
    print("当前处于第 {} 页".format(n))
    n = (n-1)*25
    url = "https://movie.douban.com/top250?start={}&filter=".format(n)
    print(url)
    reps = requests.get(url, headers=headers)
    # print(reps.text)
    html = reps.text
    # movie_resp = re.compile(r'<div class="item">.*?<span class="title">(.*?)</span>?', re.S)
    movie_resp = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)'
                            r'</span>.*?<p class="">.*?<br>(?P<year>.*?)'
                            r'&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)'
                            r'</span>.*?<span>(?P<num>.*?)人评价</span>', re.S)
    # res = movie_resp.findall(html)
    res = movie_resp.finditer(html)
    # print(res)

    # for i in res:
    #     n +=1
        # print("第{}部电影: {}".format(n, i))

    # with open("data.csv",'a',encoding="utf-8") as fp:
    #     csvwriter = csv.writer(fp)
    #
    #     for it in res:
    #
    #         # print(it.group("year").strip())
    #         # print(it.groupdict())
    #         dic = it.groupdict()
    #         dic["year"] = dic["year"].strip()
    #         print(dic)
    #         csvwriter.writerow(dic.values())

    f = open("data.csv", 'w',encoding="utf-8")
    csvwriter = csv.writer(f)
    for it in res:
        # print(it.group("year").strip())
        # print(it.groupdict())
        dic = it.groupdict()
        dic["year"] = dic["year"].strip()
        print(dic)
        csvwriter.writerow(dic.values())
    f.close()






































