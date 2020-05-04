from tkinter import *
import tkinter.messagebox
# 窗口消息弹出
root = Tk()


class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('鼠标跳出菜单')
        self.menu = Menu(self.master, tearoff=0)
        self.menu.add_command(label='提示', command=self.showClick)
        self.menu.add_command(label='退出', command=self.onExit)
        self.master.bind('<Button-3>', self.showMenu)
        self.pack()

    def showMenu(self, e):
        self.menu.post(e.x_root, e.y_root)

    def showClick(self):
        tkinter.messagebox.showinfo('鼠标点击')

    def onExit(self):
        self.quit()


root.geometry('400x500')
app = Example()
root.mainloop()
