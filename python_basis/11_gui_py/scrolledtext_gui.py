import tkinter as tk
from tkinter import scrolledtext
root = tk.Tk()
root.title('滚动文本框')
root.geometry('200x250')
s_width = 10
s_height =3
s_show = scrolledtext.ScrolledText(root,width=s_width,height=s_height,wrap=tk.WORD)
s_show.insert('insert','hello word!!!测试多行数据的滚动')
s_show.grid(column=0,columnspan=2)
root.mainloop()