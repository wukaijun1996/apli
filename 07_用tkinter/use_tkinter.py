#-*- codeing = utf-8 -*-
# @Time : 2022/3/8 21:20 
# @Author : wu
# @File : use_tkinter.py 
# @Software: PyCharm

import tkinter

window = tkinter.Tk()
window.geometry('500x300')
window.title('猜字游戏')

label = tkinter.Label(window,text='当前商品的价格是：',bg='pink',font=('楷体',16))
label.place(x=50,y=20,width=200,height=30)

price = tkinter.StringVar(value='***')
price_label = tkinter.Label(window,textvariable=price,bg='pink',font=('楷体',16))
price_label.place(x=250,y=20,width=70,height=30)

input_label = tkinter.Label(window,text='请输入猜测的的价格',bg='pink',font=('楷体',16))
input_label.place(x=50,y=60,width=200,height=30)

input_price = tkinter.Entry(window,show=None)
input_price.place(x=50,y=100,width=200,height=30)

sumbit_btn = tkinter.Button(window,text='提交',bg='pink',font=('楷体',16))
sumbit_btn.place(x=260,y=100,width=70,height=30)

message_label = tkinter.Label(window,text='提示:',bg='pink',font=('楷体',16))
message_label.place(x=290,y=230,width=200,height=30)

info = tkinter.StringVar(value='请输入商品的价格')
message = tkinter.Label(window,textvariable=info,bg='pink',font=('楷体',16))
message.place(x=290,y=260,width=200,height=30)




window.mainloop()

