#-*- codeing = utf-8 -*-
# @Time : 2022/2/9 20:53 
# @Author : wu
# @File : 2_爬取斗鱼.py 
# @Software: PyCharm

import requests
import json
import re,time,os
import multiprocessing

def get_douyu(i):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    }
    page = i

    url = f"https://www.douyu.com/gapi/rknc/directory/yzRec/{page}"

    res = requests.get(url,headers=headers,)
    # print(res.json(),type(res.json()))
    result = res.json()
    # print(result["data"]['rl'])
    if not os.path.exists("douyu"):
        os.mkdir("douyu")
    sum = 0
    for i in result["data"]['rl']:
        # print(i)
        sum += 1
        print("当前是来自颜值的{}主播，图片链接为{}".format(i['nn'],i["rs16"]))
        # pict_name = i["screenshot"].split("/")[-1]
        pict_name = f'{page}-{sum}.png'
        pict = requests.get(i["rs16"])

        with open("douyu/" + pict_name,"wb") as fp:
            fp.write(pict.content)
        time.sleep(1)


if __name__ == '__main__':

    if not os.path.exists("douyu"):
        os.mkdir("douyu")

    for i in range(1,5):
        multiprocessing.Process(target=get_douyu,args=(i,)).start()



