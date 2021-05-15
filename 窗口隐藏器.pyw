import win32gui
import easygui
import tkinter as tk
def hind():
    title = easygui.enterbox('窗口标题：')
    status = win32gui.ShowWindow(win32gui.FindWindow(0,title),0)
    if status == 24:
        easygui.msgbox('成功')
    else:
        easygui.msgbox('失败：找不到窗口')
def show():
    title = easygui.enterbox('窗口标题：')
    win32gui.ShowWindow(win32gui.FindWindow(0,title),1)
main = tk.Tk()
b_hind = tk.Button(main,text = '隐藏窗口',command = hind)
b_hind.pack()
b_show = tk.Button(main,text = '显示窗口',command = show)
b_show.pack()
main.geometry('200x70+780+470')
main.mainloop()
