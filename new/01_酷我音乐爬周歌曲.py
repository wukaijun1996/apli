#-*- codeing = utf-8 -*-
# @Time : 2022/2/24 23:25 
# @Author : wu
# @File : 01_酷我音乐爬周歌曲.py 
# @Software: PyCharm
import time

import requests


def singer_data(id = 2):
    url = f'http://www.kuwo.cn/api/www/playlist/playListInfo?pid=2867496601&pn={id}&rn=30&httpsStatus=1&reqId=7f4f4320-9586-11ec-bc24-bffc37cf9fb4'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Referer":"http://www.kuwo.cn/playlist_detail/2867496601",
        "Host": "www.kuwo.cn",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Cookie": "_ga=GA1.2.1500371689.1644328102; _gid=GA1.2.187070734.1645713403; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1644328101,1645713404; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1645716675; kw_token=CEV1KKYTQ2T",
        "csrf": "CEV1KKYTQ2T"
    }
    resp = requests.get(url,headers= headers)
    # print(resp.json())

    # http://www.kuwo.cn/api/www/playlist/playListInfo?pid=2867496601&pn=2&rn=30&httpsStatus=1&reqId=7f4f4320-9586-11ec-bc24-bffc37cf9fb4
    # http://www.kuwo.cn/api/www/playlist/playListInfo?pid=2867496601&pn=2&rn=30&httpsStatus=1&reqId=7f4f4320-9586-11ec-bc24-bffc37cf9fb4
    # http://www.kuwo.cn/api/www/playlist/playListInfo?pid=2867496601&pn=3&rn=30&httpsStatus=1&reqId=e1852b40-9586-11ec-87d8-25977b80956a

    Jay_information = resp.json()["data"]['musicList']

    data_1 = []
    for i in Jay_information:
        # print(i)
        # print(i['musicrid'].split("_")[-1] + "_" + i['name'])
        music_mid_singer = i['musicrid'].split("_")[-1] + "_" + i['name']
        data_1.append(music_mid_singer)
        # print(i['name'])     data  726836_雨下一整晚
    # print(data_1)
    return data_1

def down_music(mid,music_name):
    url_head =f"http://www.kuwo.cn/api/v1/www/music/playUrl?mid={mid}&type=mp3&httpsStatus=1&reqId=a546ab60-957f-11ec-bb21-fbaf4aed3dc5"
    # name_head = f'http://m.kuwo.cn/newh5/singles/songinfoandlrc?musicId={mid}&httpsStatus=1&reqId=219901a0-9584-11ec-bc24-bffc37cf9fb4'
    url_resp = requests.get(url_head)
    url = url_resp.json()['data']['url']
    # print(url)
    # name_resp = requests.get(name_head)
    # music_name = name_resp.json()['data']['lrclist'][0]['lineLyric']
    # print("歌曲名和歌手为：{}，链接地址为：{}".format(music_name,url))
    print("开始下载")
    with open("./music/" + music_name + ".mp3","wb") as f:
        resp_music = requests.get(url)
        f.write(resp_music.content)
        f.flush()
    time.sleep(1)
    print("下载{}完成".format(music_name))

for j in singer_data(1):
    mid = j.split("_")[0]
    music_name = j.split("_")[-1]
    down_music(mid,music_name)
print("全部下载完成")



