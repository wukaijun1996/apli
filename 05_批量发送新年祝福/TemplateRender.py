#-*- codeing = utf-8 -*-
# @Time : 2022/2/21 21:43 
# @Author : wu
# @File : TemplateRender.py 
# @Software: PyCharm

from jinja2 import Template

name = "Jack"
age = 28

template = Template("my name is {{name}} and i am {{ age }} years old;")

result = template.render(name=name,age=age)

print(result)















