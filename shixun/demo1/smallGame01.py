# -*- codeing = utf-8 -*-
# @Time : 2021/7/16 16:21
# @Author : 胡振
# @File : smallGame01.py
# @Software: PyCharm
import pygame

# Constants 常量
W, H = 1242, 2208  # 背景图宽，高
FPS = 30

#Setup 设置
pygame.init()
SCREEN = pygame.display.set_mode(W, H)
pygame.display.set_caption("简单的一个小游戏")
CLOCK = pygame.time.Clock()
background1 = pygame.image.load("img/background1.jpg")
background2 = pygame.image.load("img/background2.jpg")












# def main():
#     while True:
#         menu_window()
#         game_window()
#         end_window()
#
#
# def menu_window():
#     while True:
#         for event in pygame.event.get():
#             # 鼠标点击关闭退出游戏
#             if event.type == pygame.QUIT:
#                 quit()
#         SCREEN.blit(background1, (0, 0))
#         pygame.display.flip()
#         CLOCK.tick(FPS)
#     pass
#
# def game_window():
#     while True:
#         for event in pygame.event.get():
#             # 鼠标点击关闭退出游戏
#             if event.type == pygame.QUIT:
#                 quit()
#         SCREEN.blit(background1, (0, 0))
#         pygame.display.flip()
#         CLOCK.tick(FPS)
#     pass
#
# def end_window():
#     while True:
#         for event in pygame.event.get():
#             # 鼠标点击关闭退出游戏
#             if event.type == pygame.QUIT:
#                 quit()
#         SCREEN.blit(background1, (0, 0))
#         pygame.display.flip()
#         CLOCK.tick(FPS)
#     pass
