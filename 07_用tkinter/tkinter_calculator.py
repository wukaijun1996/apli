#-*- codeing = utf-8 -*-
# @Time : 2022/3/8 22:00 
# @Author : wu
# @File : tkinter_calculator.py 
# @Software: PyCharm

import tkinter

window = tkinter.Tk()
window.geometry('300x600')
window.title('简易计算器')

content = ''

def btn_click(data):
    global content
    # print(data)
    if data == 'clear':
        expression.set(' ')
        result.set(' ')
        content=''
    elif data == '=':
        result.set(f'{eval(content)}')
    else:
        content += data
        expression.set(content)






btn_datas = [
    ['clear','(',')','+'],
    ['7', '8', '9', '-'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '/'],
    ['**', '0', '//', '='],
]
# print(eval("1+3+5"))
for r in range(5):
    for c in range(4):
        btn = tkinter.Button(window, text=btn_datas[r][c],
                             font=('楷体',16),command=lambda x=btn_datas[r][c]:btn_click(x) )
        btn.place(x=75*c, y=300+45*r, width=75, height=45)

expression = tkinter.StringVar()
exp_label = tkinter.Label(window,textvariable=expression,bg='pink',)
exp_label.place(x=0,y=50,width=300,height=70)

result = tkinter.StringVar()
res_label = tkinter.Label(window,textvariable=result,bg='pink',)
res_label.place(x=100,y=140,width=200,height=70)


window.mainloop()