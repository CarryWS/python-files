import win32gui,win32api
while True:
    win32gui.ShowWindow(win32gui.FindWindow(0,win32api.GetConsoleTitle()),0)
    win32gui.ShowWindow(win32gui.FindWindow(0,win32api.GetConsoleTitle()),1)
