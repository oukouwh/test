from tkinter import *
from tkinter import ttk
# Notebook组件
root = Tk() # 创建 窗体实例
# 设置窗体大小
root.geometry('300x450')
root.title('Notebook')
# 创建页签实例对象
net = ttk.Notebook(root)
# 创建框架1实例
net1 = ttk.Frame(net,height=100,width=100)
# 创建框架2实例
net2 = ttk.Frame(net,height=100,width=100)
# 把框架1放在页签1上面
net.add(net1,text='页签1')
# 把框架2放在页签2上面
net.add(net2,text='页签2')
# 页签对象在窗体上的定位
net.pack()
# 启动窗体消息循环功能
root.mainloop()