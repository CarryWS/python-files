import tkinter
import pyautogui
main = tkinter.Tk()
def a():
    with open('aaa.html','w') as f:
        f.write('<html><head><meta charset=GBK></head><body><a href="https://www.bilibili.com/video/BV1DX4y1K7G3/">不要点击这个链接</a></body></html>')
        f.close()
    pyautogui.alert('不要打开同一目录下的"aaa.html"')
    main.quit()
b = tkinter.Button(main,text = '不要点击这个按钮',command = a)
b.pack()
main.geometry('500x50')
main.title('不要看这个界面的内容')
main.mainloop()
