#-*- codeing = utf-8 -*-
# @Time : 2022/2/24 22:30 
# @Author : wu
# @File : 0224.py 
# @Software: PyCharm

# http://m.kuwo.cn/newh5/singles/songinfoandlrc?musicId=118980&httpsStatus=1&reqId=ff6ada90-9583-11ec-8ba0-d5d28bd4889d
# http://m.kuwo.cn/newh5/singles/songinfoandlrc?musicId=661304&httpsStatus=1&reqId=219901a0-9584-11ec-bc24-bffc37cf9fb4
# 酷我音乐歌曲请求url:      3244328    118980
# http://www.kuwo.cn/api/v1/www/music/playUrl?mid=140064959&type=music&httpsStatus=1&reqId=a546ab60-957f-11ec-bb21-fbaf4aed3dc5
# http://www.kuwo.cn/api/v1/www/music/playUrl?mid=198554068&type=music&httpsStatus=1&reqId=b6b4af91-9580-11ec-a25b-d7fa3fe7ed56
import requests


def down_music(mid):
    url_head =f"http://www.kuwo.cn/api/v1/www/music/playUrl?mid={mid}&type=mp3&httpsStatus=1&reqId=a546ab60-957f-11ec-bb21-fbaf4aed3dc5"
    name_head = f'http://m.kuwo.cn/newh5/singles/songinfoandlrc?musicId={mid}&httpsStatus=1&reqId=219901a0-9584-11ec-bc24-bffc37cf9fb4'
    url_resp = requests.get(url_head)
    url = url_resp.json()['data']['url']
    # print(url)
    name_resp = requests.get(name_head)
    music_name = name_resp.json()['data']['lrclist'][0]['lineLyric']
    print("歌曲名和歌手为：{}，链接地址为：{}".format(music_name,url))


if __name__ == '__main__':


    down = down_music(118980)




