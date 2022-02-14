#-*- codeing = utf-8 -*-
# @Time : 2022/2/8 22:14 
# @Author : wu
# @File : 1_爬取虎牙.py 
# @Software: PyCharm

import requests
import json
import re,time

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}
page = 1

url = f'https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=1663&tagAll=0&callback=getLiveListJsonpCallback&page={page}'

res = requests.get(url,headers=headers,)
# res.encoding = "utf-8"
content = res.text

#截取json数据
result = content[len('getLiveListJsonpCallback('):-1]
# print(result,type(result))

# obj = re.compile(r"getLiveListJsonpCallback(.*)")
# ret= obj.findall(content)
# print(ret[0].strip("(").strip(")"),type(result))
#
# if result == ret[0].strip("(").strip(")"):
#     print("一样了")

result2 = json.loads(result)
# print(result2,type(result2))
sum = 0
for i in result2['data']['datas']:
    sum += 1
    print("当前是来自星秀的{}主播，图片链接为{}".format(i['nick'],i["screenshot"]))
    # pict_name = i["screenshot"].split("/")[-1]
    pict_name = str(sum) + '.jpg'
    pict = requests.get(i["screenshot"])
    with open("huya/" + pict_name,"wb") as fp:
        fp.write(pict.content)
    time.sleep(1)