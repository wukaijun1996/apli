#-*- codeing = utf-8 -*-
# @Time : 2022/2/21 21:48 
# @Author : wu
# @File : TemplateRenderFile.py 
# @Software: PyCharm

from jinja2 import Template

name = "Bob"
content = open("index.html", encoding="utf-8").read()

template = Template(content)

result = template.render(name=name)

print(result)









