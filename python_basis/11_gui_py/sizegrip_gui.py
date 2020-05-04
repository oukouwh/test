from tkinter import *
from tkinter import ttk
# 窗体大小拉伸组件
root = Tk()
root.title('窗体大小拉伸组件')
ttk.Sizegrip(root).grid(row=99,column=99,sticky='se')
root.columnconfigure(0,weight=1,minsize=99)
root.rowconfigure(0,weight=1,minsize=99)
root.mainloop()