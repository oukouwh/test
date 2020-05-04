import tkinter.tix
from tkinter.constants import *
# DirList组件使用案例
root = tkinter.tix.Tk()
# 窗体名
root.title('tix组件案例')
root.geometry('500x150')
# 创建框架实例
top = tkinter.tix.Frame(root, relief=RAISED, bd=1)
# 组件在窗体上的定位
top.pack(side='left')
# 创建dirList实例
top.dir = tkinter.tix.DirTree(top)
# 设置dirlist宽度
top.dir.hlist['width'] = 30
# dirlist在窗体上的定位
top.dir.pack(side='left')
# 创建button实例
top.btn = tkinter.tix.Button(top, text='>>', pady=0)
top.btn.pack(side='left')
# c创建LabelEntry实例
top.ent = tkinter.tix.LabelEntry(top,label='安装路径：',labelside='top')
top.ent.pack(side='left')
root.mainloop()