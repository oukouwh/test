from tkinter import *
from tkinter import ttk
import time
# 进度条组件
root = Tk()
root.title('进度条案例')
root.geometry('300x450')
# 创建进度条实例
pro1 = ttk.Progressbar(root, length=150, mode='determinate', orient=HORIZONTAL)
pro1.grid(row=1, column=1)
pro1['value'] = 0 # 进度条实际进度开始位置
for i in range(100):
    pro1['value']= i + 1
    root.update() 
    time.sleep(0.1) # 循环一次进程停顿0.1秒
root.mainloop()
