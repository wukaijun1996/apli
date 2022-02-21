#-*- codeing = utf-8 -*-
# @Time : 2022/2/21 21:53 
# @Author : wu
# @File : GreetingMail.py 
# @Software: PyCharm

import yagmail
from jinja2 import Template

def send_mail(receivers,subject,body):
    yag = yagmail.SMTP(
        host='smtp.163.com', user='wu1172917145@163.com',
        password='IGEWLWEDJNGBSTBT', smtp_ssl=True
    )
    yag.send(receivers,subject,body)
    print("邮件发送成功")

bless_infos = {
    "wu1172917145@163.com,1172917145@qq.com":{
        "template":"index.html",
        "title":"虎虎生威",
        "bless":"虎年虎虎兴隆",
        "name":"Nick"
    },
    "1175647233@qq.com": {
        "template": "index.html",
        "title": "虎虎生威",
        "bless": "虎年虎虎兴隆",
        "name": "Nick"
    }
}

for mail in bless_infos:
    template = Template(open(bless_infos[mail]["template"],encoding="utf-8").read())
    body = template.render(bless_infos[mail])
    send_mail(mail.split(","),bless_infos[mail]["title"],body)


















