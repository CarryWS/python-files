import tkinter as tk
import random
for i in range(100):
    tk.Tk().geometry(str(random.randint(100,1000))+'x'+str(random.randint(100,1000))+'+'+str(random.randint(1,1024))+'+'+str(random.randint(1,1080)))

tk.Tk().mainloop()