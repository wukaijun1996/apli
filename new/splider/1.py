#-*- codeing = utf-8 -*-
# @Time : 2022/1/8 15:05 
# @Author : wu
# @File : 1.py 
# @Software: PyCharm
import time

from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


web = Chrome()
web.maximize_window()
web.implicitly_wait(30)
# web.get("https://ys.endata.cn/Information/Publish/WillSHow")

# sel_el = web.find_element(By.XPATH,'//*[@id="app"]/section/main/div/div[1]/div/section/div[1]/div[2]/div/div[1]/div[1]/div/div/input').click()
#
# web.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/ul/li[2]').click()
# # sel = Select(sel_el)
# #
# # for i in range(len(sel.options)):
# #     sel.select_by_index(2)
# # # //*[@id="pane-first"]/div[1]/div[2]
#
# xx = web.find_element(By.XPATH,'//*[@id="pane-first"]/div[1]/div[2]')
# print(xx.text)
# time.sleep(20)

web.get('https://www.w3school.com.cn/tiy/t.asp?f=eg_html_select')

web.find_element(By.XPATH,'//*[@id="tiy_btn_tryit"]/a').click()
print("hiihi")
web.find_element(By.XPATH,'/html/body/select')
print(22)
# sel_el = web.find_element(By.XPATH,'/html/body/select')
#
# sel = Select(sel_el)
#
# for i in range(len(sel.options)):
#     sel.select_by_index(i)

# /html/body/select

time.sleep(2)





