#-*- codeing = utf-8 -*-
# @Time : 2022/2/21 21:23 
# @Author : wu
# @File : SendMail.py 
# @Software: PyCharm
# wu1172917145@163
# IGEWLWEDJNGBSTBT
import yagmail

receivers = ["wu1172917145@163.com","1172917145@qq.com"]
subject = "第二次祝福测试"
body = "新年到了，恭喜发财"

yag = yagmail.SMTP(
    host='smtp.163.com',user='wu1172917145@163.com',
    password='IGEWLWEDJNGBSTBT',smtp_ssl=True
)

yag.send(receivers,subject,body)

print("发送成功")
