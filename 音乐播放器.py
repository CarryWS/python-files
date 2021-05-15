import pygame
import time
import easygui as g
from pygame.locals import *
def play(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(start = 0.0)
    time.sleep(300)
    pygame.mixer.music.stop()
music = g.buttonbox('请选择音频路径','提示',('浏览','输入路径'))
if music == '浏览':
    musicpath = g.fileopenbox('选择文件')
    if musicpath == None:
        g.msgbox('你还没有选择')
    else:
        play(musicpath)
else:
    musicpath = g.enterbox('请输入音频文件路径','提示')
    if musicpath == None:
        g.msgbox('你还没有选择')
    else:
        play(musicpath)

