#-*- codeing = utf-8 -*-
# @Time : 2022/2/14 21:37 
# @Author : wu
# @File : PyGameSnew.py 
# @Software: PyCharm

import pygame
import random

# 初始化Pygame
pygame.init()

SIZE = (1080,736)

# 使用指定尺寸初始化画布
screen = pygame.display.set_mode(SIZE)
# 对弹出的窗口添加标题
pygame.display.set_caption("Snow Animation")
# 图片位置
bg = pygame.image.load("111.jpeg")

# 雪花列表
snow_list = []

# 初始化雪花
for i in range(200):
    x = random.randrange(0,SIZE[0])
    y = random.randrange(0,SIZE[1])
    sx = random.randint(-1,1)
    sy = random.randint(6,16)
    size = random.randint(1,2)
    snow_list.append([x,y,sx,sy,size])
print(snow_list)
# 使用时钟实现切换绘制界面的切换
clock = pygame.time.Clock()

done = False
while not done:
    # 消息事件循环，判断退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # 图片背景
    screen.blit(bg,(0,0))
    # 雪花列表循环
    for i in range(len(snow_list)):
        # 绘制雪花 颜色 位置 大小
        pygame.draw.circle(screen,(255,255,255),snow_list[i][:2],size)

        snow_list[i][0] += snow_list[i][2]
        snow_list[i][1] += snow_list[i][3]

        if snow_list[i][1] > SIZE[1]:
            snow_list[i][1] = random.randrange(-50,-10)
            snow_list[i][0] = random.randrange(0,SIZE[0])

    # 刷新屏幕
    pygame.display.flip()
    clock.tick(20)

# 退出
pygame.quit()




